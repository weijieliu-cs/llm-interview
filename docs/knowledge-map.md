# 知识点导航

[返回首页](../README.md) · [题目索引](question-bank.md) · [参考项目对照](reference-projects.md)

这里按知识点定位答案，不要求按章节编号依次阅读。每项都链接到已编写的内容。

| 方向 | 知识点 | 阅读与练习 |
| --- | --- | --- |
| 数学与损失 | Softmax、温度、交叉熵、PPL、梯度 | [F01](01-fundamentals.md#f01)、[F02](01-fundamentals.md#f02)、[I05](07-inference.md#i05) |
| 优化与泛化 | AdamW、warmup、归一化、过拟合 | [F03](01-fundamentals.md#f03)、[F04](01-fundamentals.md#f04)、[F06](01-fundamentals.md#f06) |
| NLP 与分词 | BPE、WordPiece、Unigram、字节级、Word2Vec、BERT | [F05](01-fundamentals.md#f05)、[N01](11-nlp-and-embeddings.md#n01)、[N02](11-nlp-and-embeddings.md#n02) |
| Transformer | Q/K/V、因果掩码、复杂度、Pre/Post-Norm、FFN | [T01](02-transformer.md#t01)、[T02](02-transformer.md#t02)、[Attention 实现](../examples/attention.py) |
| 结构变体 | RoPE、MHA/MQA/GQA、MoE、视觉连接器、模型比较 | [T03](02-transformer.md#t03)、[T04](02-transformer.md#t04)、[T05](02-transformer.md#t05)、[T06](02-transformer.md#t06)、[N06](11-nlp-and-embeddings.md#n06) |
| 预训练 | CLM/MLM、数据清洗、去重、污染、Scaling Law | [P01](03-pretraining.md#p01)、[P02](03-pretraining.md#p02)、[P03](03-pretraining.md#p03) |
| 训练稳定性 | loss spike、NaN、长上下文、断点恢复 | [P04](03-pretraining.md#p04)、[P05](03-pretraining.md#p05)、[P06](03-pretraining.md#p06) |
| SFT 与 PEFT | 训练阶段、标签 shift、loss mask、packing、LoRA、QLoRA | [S01](04-finetuning.md#s01)、[S02](04-finetuning.md#s02)、[S03](04-finetuning.md#s03)、[S04](04-finetuning.md#s04) |
| 微调实验 | 数据与超参数消融、遗忘、模板不一致 | [S05](04-finetuning.md#s05)、[S06](04-finetuning.md#s06)、[X02](10-system-design.md#x02) |
| 强化学习与对齐 | 奖励模型、RLHF、PPO、DPO、GRPO、reward hacking | [A01](05-alignment.md#a01)、[A02](05-alignment.md#a02)、[A03](05-alignment.md#a03)、[A04](05-alignment.md#a04)、[A06](05-alignment.md#a06) |
| 推理能力 | 推理预算、蒸馏、CoT、自一致性、pass@k | [A05](05-alignment.md#a05)、[C02](12-prompt-and-context.md#c02)、[E04](09-evaluation.md#e04) |
| 分布式训练 | DP/TP/PP/EP、ZeRO、梯度累积、激活重计算、OOM | [D01—D06](06-distributed-training.md) |
| 推理加速 | prefill/decode、KV Cache、FlashAttention、PagedAttention | [I01](07-inference.md#i01)、[I02](07-inference.md#i02)、[I03](07-inference.md#i03) |
| 服务与压缩 | 量化、连续批处理、前缀缓存、推测解码、SLA | [I04](07-inference.md#i04)、[I06](07-inference.md#i06)、[X03](10-system-design.md#x03) |
| 检索表示 | 对比学习、难负例、双塔、余弦、Cross-encoder | [N03](11-nlp-and-embeddings.md#n03)、[N04](11-nlp-and-embeddings.md#n04)、[N05](11-nlp-and-embeddings.md#n05) |
| RAG | RAG/SFT 选型、切分、混合检索、重排、oracle-context | [R01](08-rag-and-agents.md#r01)、[R02](08-rag-and-agents.md#r02)、[R03](08-rag-and-agents.md#r03)、[R04](08-rag-and-agents.md#r04) |
| Agent 与工具 | 工作流、终止条件、重试、幂等、权限、提示注入、MCP | [R05](08-rag-and-agents.md#r05)、[R06](08-rag-and-agents.md#r06)、[C04](12-prompt-and-context.md#c04)、[C05](12-prompt-and-context.md#c05) |
| 上下文工程 | Zero/Few-shot、历史摘要、记忆、预算、提示词回归 | [C01](12-prompt-and-context.md#c01)、[C03](12-prompt-and-context.md#c03)、[C06](12-prompt-and-context.md#c06) |
| 评测与可靠性 | 评测集、Recall/MRR/nDCG、Judge、A/B、幻觉与拒答 | [E01—E06](09-evaluation.md)、[指标实现](../examples/retrieval_metrics.py) |
| 项目与系统 | 企业知识库、低资源训练、容量规划、回滚、消融、项目表达 | [X01—X06](10-system-design.md)、[模拟面试](interview-practice.md) |
