"""单 query 检索指标；分级相关性使用 0—3，宏平均由调用者完成。"""

import math
from typing import Dict, Mapping, Sequence


def evaluate_ranking(
    ranked_ids: Sequence[str], relevance: Mapping[str, int], k: int
) -> Dict[str, float]:
    """计算前 k 项的 precision、recall、hit、reciprocal_rank 和 nDCG。

    未标注文档视为不相关；重复 ID 仍占据原排名，但仅首次出现获得增益。
    空相关集合的 recall/nDCG 定义为 0；结果不足 k 项时 precision 仍除以 k。
    这是显式选择的评测口径，不是所有评测工具的统一默认值。
    """
    if type(k) is not int or k <= 0:
        raise ValueError("k must be a positive integer")
    if any(type(grade) is not int or not 0 <= grade <= 3 for grade in relevance.values()):
        raise ValueError("relevance grades must be integers from 0 to 3")

    relevant = {doc_id for doc_id, grade in relevance.items() if grade > 0}
    seen = set()
    hits = 0
    reciprocal_rank = 0.0
    dcg = 0.0
    for rank, doc_id in enumerate(ranked_ids[:k], start=1):
        if doc_id in seen:
            continue
        seen.add(doc_id)
        grade = relevance.get(doc_id, 0)
        if grade > 0:
            hits += 1
            if reciprocal_rank == 0.0:
                reciprocal_rank = 1.0 / rank
            dcg += (2 ** grade - 1) / math.log2(rank + 1)

    ideal_grades = sorted(relevance.values(), reverse=True)[:k]
    ideal_dcg = sum(
        (2 ** grade - 1) / math.log2(rank + 1)
        for rank, grade in enumerate(ideal_grades, start=1)
    )
    return {
        "precision": hits / k,
        "recall": hits / len(relevant) if relevant else 0.0,
        "hit": float(hits > 0),
        "reciprocal_rank": reciprocal_rank,
        "ndcg": dcg / ideal_dcg if ideal_dcg else 0.0,
    }


if __name__ == "__main__":
    cutoff = 3
    rankings = [
        (["d2", "d1", "d1"], {"d1": 3, "d3": 1}),
        (["d3", "d1", "d2"], {"d1": 3, "d3": 1}),
    ]
    results = [evaluate_ranking(ranking, labels, cutoff) for ranking, labels in rankings]
    for query_number, metrics in enumerate(results, start=1):
        print("Query {}: {}".format(query_number, {
            name: round(value, 4) for name, value in metrics.items()
        }))
    mrr = sum(result["reciprocal_rank"] for result in results) / len(results)
    print("MRR@{}: {:.4f}".format(cutoff, mrr))
