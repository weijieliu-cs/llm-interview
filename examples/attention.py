"""单头 Attention 的教学实现；不包含投影、batch、dropout 或自动求导。"""

import math
from typing import List, Sequence, Tuple


Matrix = Sequence[Sequence[float]]


def stable_softmax(scores: Sequence[float]) -> List[float]:
    """允许 -inf 表示屏蔽；空输入、全屏蔽、NaN 和 +inf 均报错。"""
    if not scores:
        raise ValueError("scores must not be empty")
    if any(math.isnan(x) or x == math.inf for x in scores):
        raise ValueError("scores must not contain NaN or +inf")
    maximum = max(scores)
    if maximum == -math.inf:
        raise ValueError("at least one score must be unmasked")
    weights = [math.exp(x - maximum) for x in scores]
    total = sum(weights)
    return [x / total for x in weights]


def _validate_matrix(matrix: Matrix, name: str) -> int:
    if not matrix or not matrix[0]:
        raise ValueError("{} must be a non-empty matrix".format(name))
    width = len(matrix[0])
    if any(len(row) != width for row in matrix):
        raise ValueError("{} must be rectangular".format(name))
    if any(not math.isfinite(x) for row in matrix for x in row):
        raise ValueError("{} must contain finite values".format(name))
    return width


def scaled_dot_product_attention(
    query: Matrix,
    key: Matrix,
    value: Matrix,
    causal: bool = False,
    query_start: int = 0,
) -> Tuple[List[List[float]], List[List[float]]]:
    """返回 (output, weights)，形状为 [S_q, d_v] 和 [S_q, S_k]。

    因果模式只允许 key_index <= query_start + query_index。
    query_start 表示当前 query 在完整序列中的起始位置，可用于增量验证。
    Python 循环用于展示公式，不适合实际 GPU 训练或线上推理。
    """
    dimension = _validate_matrix(query, "query")
    key_dimension = _validate_matrix(key, "key")
    value_dimension = _validate_matrix(value, "value")
    if dimension != key_dimension or len(key) != len(value):
        raise ValueError("Q/K dimensions and K/V sequence lengths must match")
    if type(query_start) is not int or query_start < 0:
        raise ValueError("query_start must be a non-negative integer")

    output = []
    all_weights = []
    scale = math.sqrt(dimension)
    for query_index, query_row in enumerate(query):
        scores = []
        for key_index, key_row in enumerate(key):
            if causal and key_index > query_start + query_index:
                scores.append(-math.inf)
            else:
                scores.append(sum(q * k for q, k in zip(query_row, key_row)) / scale)
        weights = stable_softmax(scores)
        output.append([
            sum(weight * value_row[column] for weight, value_row in zip(weights, value))
            for column in range(value_dimension)
        ])
        all_weights.append(weights)
    return output, all_weights


if __name__ == "__main__":
    q = [[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]]
    k = [[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]]
    v = [[10.0, 0.0], [0.0, 10.0], [5.0, 5.0]]
    result, attention_weights = scaled_dot_product_attention(q, k, v, causal=True)
    print("Causal attention weights:")
    for row in attention_weights:
        print([round(x, 4) for x in row])
    print("Output:")
    for row in result:
        print([round(x, 4) for x in row])
