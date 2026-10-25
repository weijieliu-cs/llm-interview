# 面试题索引

[返回首页](../README.md) · [知识点导航](knowledge-map.md) · [学习路线](learning-roadmap.md)

共 72 道按知识点整理的练习题，每题包含回答要点与追问。P0 为优先掌握，P1 为专题展开；优先级是复习建议，不是公司真题或出现频率统计。

## 01 数学与机器学习基础

| 题号 | 知识点 / 问题 | 优先级 |
| --- | --- | --- |
| [F01](01-fundamentals.md#f01) | 为什么 Softmax 要减去最大值？ | P0 |
| [F02](01-fundamentals.md#f02) | 交叉熵和困惑度是什么关系？ | P0 |
| [F03](01-fundamentals.md#f03) | LayerNorm、RMSNorm 和 BatchNorm 有什么区别？ | P0 |
| [F04](01-fundamentals.md#f04) | AdamW 为什么把权重衰减与梯度更新分开？ | P1 |
| [F05](01-fundamentals.md#f05) | BPE、WordPiece、Unigram 与字节级分词如何比较？ | P0 |
| [F06](01-fundamentals.md#f06) | 训练损失持续下降但验证效果变差，如何分析？ | P0 |

## 02 Transformer 与模型结构

| 题号 | 知识点 / 问题 | 优先级 |
| --- | --- | --- |
| [T01](02-transformer.md#t01) | Attention 为什么除以根号下的单头维度？ | P0 |
| [T02](02-transformer.md#t02) | Pre-Norm 与 Post-Norm 如何比较？ | P0 |
| [T03](02-transformer.md#t03) | RoPE 为什么能体现相对位置？ | P0 |
| [T04](02-transformer.md#t04) | MHA、MQA、GQA 的差别是什么？ | P0 |
| [T05](02-transformer.md#t05) | Encoder、Decoder 和多模态连接结构如何选择？ | P1 |
| [T06](02-transformer.md#t06) | MoE 为什么参数量大但激活计算量较小？ | P1 |

## 03 预训练与数据

| 题号 | 知识点 / 问题 | 优先级 |
| --- | --- | --- |
| [P01](03-pretraining.md#p01) | CLM、MLM 和去噪目标有什么区别？ | P0 |
| [P02](03-pretraining.md#p02) | 如何设计预训练数据治理流程？ | P0 |
| [P03](03-pretraining.md#p03) | 固定算力预算下如何选择参数量和训练 token 数？ | P1 |
| [P04](03-pretraining.md#p04) | 训练突然出现 loss spike 或 NaN，怎么排查？ | P0 |
| [P05](03-pretraining.md#p05) | 如何把短上下文模型扩展到更长上下文？ | P1 |
| [P06](03-pretraining.md#p06) | 怎样实现可恢复、可比较的训练实验？ | P1 |

## 04 SFT 与参数高效微调

| 题号 | 知识点 / 问题 | 优先级 |
| --- | --- | --- |
| [S01](04-finetuning.md#s01) | 持续预训练、SFT 和偏好优化如何选择？ | P0 |
| [S02](04-finetuning.md#s02) | SFT 的 loss mask、padding 和 packing 容易出什么错？ | P0 |
| [S03](04-finetuning.md#s03) | LoRA 的原理、参数量和合并条件是什么？ | P0 |
| [S04](04-finetuning.md#s04) | QLoRA 是否把所有训练计算都变成 4 bit？ | P0 |
| [S05](04-finetuning.md#s05) | 如何设计一轮有结论的微调实验？ | P0 |
| [S06](04-finetuning.md#s06) | 微调后答非所问或通用能力下降，如何定位？ | P0 |

## 05 偏好对齐与推理能力

| 题号 | 知识点 / 问题 | 优先级 |
| --- | --- | --- |
| [A01](05-alignment.md#a01) | 经典 RLHF 流程包含哪些阶段？ | P0 |
| [A02](05-alignment.md#a02) | DPO 的损失为什么包含参考模型？ | P0 |
| [A03](05-alignment.md#a03) | PPO 中旧策略、参考策略与价值模型分别做什么？ | P1 |
| [A04](05-alignment.md#a04) | GRPO 如何避免独立价值模型？ | P1 |
| [A05](05-alignment.md#a05) | 推理时增加计算、强化学习和蒸馏是什么关系？ | P1 |
| [A06](05-alignment.md#a06) | 如何发现并缓解 reward hacking？ | P0 |

## 06 分布式训练

| 题号 | 知识点 / 问题 | 优先级 |
| --- | --- | --- |
| [D01](06-distributed-training.md#d01) | 如何估算全参数训练的模型状态显存？ | P0 |
| [D02](06-distributed-training.md#d02) | 什么时候选择 DP、TP、PP 或 EP？ | P0 |
| [D03](06-distributed-training.md#d03) | ZeRO 的三个阶段分别切分什么？ | P0 |
| [D04](06-distributed-training.md#d04) | 梯度累积如何影响有效 batch 与损失归约？ | P0 |
| [D05](06-distributed-training.md#d05) | GPU 利用率低但没有 OOM，如何定位瓶颈？ | P1 |
| [D06](06-distributed-training.md#d06) | OOM 时如何按来源选择优化手段？ | P0 |

## 07 推理优化与部署

| 题号 | 知识点 / 问题 | 优先级 |
| --- | --- | --- |
| [I01](07-inference.md#i01) | Prefill 和 Decode 的瓶颈有什么区别？ | P0 |
| [I02](07-inference.md#i02) | 算一次 GQA 的 KV Cache 显存需要哪些条件？ | P0 |
| [I03](07-inference.md#i03) | FlashAttention 和 PagedAttention 分别解决什么问题？ | P0 |
| [I04](07-inference.md#i04) | INT8、INT4 量化如何影响速度与质量？ | P1 |
| [I05](07-inference.md#i05) | 温度、Top-k、Top-p、贪心和 Beam Search 如何比较？ | P0 |
| [I06](07-inference.md#i06) | 连续批处理、前缀缓存和推测解码如何取舍？ | P1 |

## 08 RAG 与 Agent

| 题号 | 知识点 / 问题 | 优先级 |
| --- | --- | --- |
| [R01](08-rag-and-agents.md#r01) | 什么时候用 RAG，什么时候用微调？ | P0 |
| [R02](08-rag-and-agents.md#r02) | 如何设计文档切分和索引？ | P0 |
| [R03](08-rag-and-agents.md#r03) | 为什么组合稀疏检索、稠密检索和重排？ | P0 |
| [R04](08-rag-and-agents.md#r04) | RAG 答错时如何判断是哪一环的问题？ | P0 |
| [R05](08-rag-and-agents.md#r05) | 什么任务值得使用 Agent？ | P1 |
| [R06](08-rag-and-agents.md#r06) | 如何处理 RAG 和工具调用中的权限与提示注入？ | P0 |

## 09 评测与可靠性

| 题号 | 知识点 / 问题 | 优先级 |
| --- | --- | --- |
| [E01](09-evaluation.md#e01) | 如何构造可信的业务评测集？ | P0 |
| [E02](09-evaluation.md#e02) | Recall@k、MRR 和 nDCG 分别衡量什么？ | P0 |
| [E03](09-evaluation.md#e03) | BLEU、ROUGE、LLM-as-a-Judge 能否替代人工判断？ | P0 |
| [E04](09-evaluation.md#e04) | pass@k 与单次准确率怎么比较？ | P1 |
| [E05](09-evaluation.md#e05) | 如何判断离线提升是否可信、能否上线？ | P0 |
| [E06](09-evaluation.md#e06) | 怎样评估幻觉、拒答与信息泄漏？ | P0 |

## 10 系统设计与场景题

| 题号 | 知识点 / 问题 | 优先级 |
| --- | --- | --- |
| [X01](10-system-design.md#x01) | 如何设计一个企业内部知识库问答系统？ | P0 |
| [X02](10-system-design.md#x02) | 一张 24 GiB GPU 上如何做 7B 模型微调？ | P0 |
| [X03](10-system-design.md#x03) | 要求 100 QPS 的模型服务需要多少 GPU？ | P0 |
| [X04](10-system-design.md#x04) | 上线后正确率下降且 P95 延迟升高，怎么处理？ | P0 |
| [X05](10-system-design.md#x05) | 如何证明微调或 RAG 改动的收益来自关键设计？ | P0 |
| [X06](10-system-design.md#x06) | 如何向面试官讲清楚一个真实项目？ | P0 |

## 11 经典 NLP、Embedding 与模型比较

| 题号 | 知识点 / 问题 | 优先级 |
| --- | --- | --- |
| [N01](11-nlp-and-embeddings.md#n01) | Word2Vec 的 CBOW 与 Skip-gram 有什么区别？ | P1 |
| [N02](11-nlp-and-embeddings.md#n02) | BERT 的 MLM 为什么不直接适合自回归生成？ | P1 |
| [N03](11-nlp-and-embeddings.md#n03) | 如何训练面向检索的 Embedding 模型？ | P0 |
| [N04](11-nlp-and-embeddings.md#n04) | 余弦、内积、欧氏距离什么时候给出相同排序？ | P0 |
| [N05](11-nlp-and-embeddings.md#n05) | 为什么召回常用双塔，重排常用交叉编码器？ | P0 |
| [N06](11-nlp-and-embeddings.md#n06) | 如何专业地比较不同模型家族与具体版本？ | P1 |

## 12 提示词与上下文工程

| 题号 | 知识点 / 问题 | 优先级 |
| --- | --- | --- |
| [C01](12-prompt-and-context.md#c01) | Zero-shot、Few-shot 和指令微调如何区别？ | P0 |
| [C02](12-prompt-and-context.md#c02) | CoT 和 Self-consistency 如何使用及评估？ | P1 |
| [C03](12-prompt-and-context.md#c03) | 长对话的上下文预算如何管理？ | P0 |
| [C04](12-prompt-and-context.md#c04) | Function Calling、MCP 和 Agent 是什么关系？ | P1 |
| [C05](12-prompt-and-context.md#c05) | 如何选择 LangChain 等框架或直接编排？ | P1 |
| [C06](12-prompt-and-context.md#c06) | 如何持续维护提示词而不在测试集上过拟合？ | P0 |
