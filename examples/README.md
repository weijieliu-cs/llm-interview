# 代码练习

[返回首页](../README.md) · [知识点导航](../docs/knowledge-map.md)

环境：Python 3.8+，仅使用标准库，无需安装依赖。代码展示公式与边界条件，不实现完整模型，也不代替生产环境的张量算子或评测框架。

## 练习一：因果注意力

先独立完成以下要求，再查看 [attention.py](attention.py)：

1. 接收二维 Q、K、V，计算缩放点积、Softmax 与加权输出。
2. 用负无穷屏蔽未来位置，说明为什么在 Softmax 前应用 mask。
3. 修改未来 K/V，证明之前位置的输出不变。
4. 只取最后一个 query，设置其真实位置偏移，验证结果与完整因果计算的最后一行一致。

```bash
python3 examples/attention.py
```

返回输出形状为 `[S_q, d_v]`，权重形状为 `[S_q, S_k]`。默认 `query_start=0` 的因果掩码适用于从序列开头开始的 query；增量 query 需传入正确偏移。代码不包括 K/V 投影或真实缓存管理，增量测试只是验证注意力计算与位置的关系。

进一步可用张量库实现 batch、多头、padding mask 和反向传播；矩形因果掩码在不同接口的对齐约定可能不同，核对 [PyTorch SDPA 文档](https://docs.pytorch.org/docs/stable/generated/torch.nn.functional.scaled_dot_product_attention.html)。

关联问题：[T01](../docs/02-transformer.md#t01)、[T04](../docs/02-transformer.md#t04)、[I02](../docs/07-inference.md#i02)。

## 练习二：检索指标

给定候选 ID 排名和 0—3 的相关性标注，实现 [retrieval_metrics.py](retrieval_metrics.py) 中的指标，解释“只召回一篇”与“覆盖所有相关证据”的差异。

```bash
python3 examples/retrieval_metrics.py
```

示例包含两个 query，宏平均 `MRR@3` 为 `0.7500`。代码显式规定：

- 重复 ID 占据排名，只首次命中得分，防止重复结果虚增指标。
- 未标注文档视为不相关；实际数据标注不完整时，需另行评估该假设的影响。
- 无相关标注的 query 返回 0，不在函数内部自动跳过。
- Precision@k 的分母固定为 k，结果不足 k 项也不改变分母。
- 函数返回的是单 query 的倒数排名；多个 query 的平均值才是 MRR。

关联问题：[E02](../docs/09-evaluation.md#e02)、[R04](../docs/08-rag-and-agents.md#r04)。

## 检查

```bash
python3 -m unittest discover -s tests -v
```

测试关注因果隔离、增量等价、数值稳定、重复排名、空相关集合和分级排序。练习可扩展为 BM25/向量检索结果的离线比较，但不应把这里的教学样例分数写成真实项目指标。
