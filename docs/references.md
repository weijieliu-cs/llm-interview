# 论文与官方资料

[返回首页](../README.md) · [知识点导航](knowledge-map.md) · [参考项目对照](reference-projects.md)

资料整理日期：**2026-10-25**。论文用于核对原始定义与实验条件，工具文档用于确认接口语义。下面是本指南已引用的阅读入口；不将旧论文中的性能数字作为当前工具的能力保证。

## 基础、表示与结构

| 资料 | 阅读重点 |
| --- | --- |
| [Attention Is All You Need](https://arxiv.org/abs/1706.03762) | 缩放点积注意力、多头、编码器与解码器 |
| [Decoupled Weight Decay Regularization](https://arxiv.org/abs/1711.05101) | AdamW 与 L2 正则的区别 |
| [On Layer Normalization in the Transformer Architecture](https://arxiv.org/abs/2002.04745) | Pre-Norm、Post-Norm 与训练稳定性 |
| [RoFormer](https://arxiv.org/abs/2104.09864) | 旋转位置编码与相对位置关系 |
| [GQA](https://arxiv.org/abs/2305.13245) | 查询头与 KV 头的分组共享 |
| [Switch Transformers](https://arxiv.org/abs/2101.03961) | 稀疏专家、路由与训练挑战 |
| [Word2Vec](https://arxiv.org/abs/1301.3781) | CBOW 与 Skip-gram 表示学习 |
| [BERT](https://arxiv.org/abs/1810.04805) | 双向表示和预训练目标 |
| [Sentence-BERT](https://arxiv.org/abs/1908.10084) | 句向量与双塔结构 |
| [LLaMA](https://arxiv.org/abs/2302.13971) | 阅读具体模型的结构和训练设置 |
| [DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437) | MoE、注意力设计与系统协同 |
| [Visual Instruction Tuning](https://arxiv.org/abs/2304.08485) | 视觉编码器与语言模型连接、指令训练 |

## 训练、微调与对齐

| 资料 | 阅读重点 |
| --- | --- |
| [Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556) | 固定训练预算下的模型与数据分配 |
| [LoRA](https://arxiv.org/abs/2106.09685) | 低秩增量、参数量和合并 |
| [QLoRA](https://arxiv.org/abs/2305.14314) | 量化基座与低秩适配器 |
| [InstructGPT](https://arxiv.org/abs/2203.02155) | 示范、偏好与强化学习的经典流程 |
| [PPO](https://arxiv.org/abs/1707.06347) | 重要性比率、裁剪和价值估计 |
| [DPO](https://arxiv.org/abs/2305.18290) | 参考策略、偏好对与损失推导 |
| [DeepSeekMath](https://arxiv.org/html/2402.03300v3) | GRPO、组内相对优势 |
| [DeepSeek-R1](https://arxiv.org/abs/2501.12948) | 推理能力训练、奖励及蒸馏 |
| [ZeRO](https://arxiv.org/abs/1910.02054) | 模型状态冗余与分片 |

## 推理与压缩

| 资料 | 阅读重点 |
| --- | --- |
| [FlashAttention](https://arxiv.org/abs/2205.14135) | IO 感知分块、精确注意力 |
| [PagedAttention](https://arxiv.org/abs/2309.06180) | KV 存储管理与请求共享 |
| [GPTQ](https://arxiv.org/abs/2210.17323) | 训练后权重量化 |
| [AWQ](https://arxiv.org/abs/2306.00978) | 激活感知的权重量化 |
| [The Curious Case of Neural Text Degeneration](https://arxiv.org/abs/1904.09751) | Nucleus Sampling 与生成退化 |
| [Speculative Decoding](https://arxiv.org/abs/2211.17192) | 草稿生成、目标验证和分布保持 |

## 应用、评测与可靠性

| 资料 | 阅读重点 |
| --- | --- |
| [Retrieval-Augmented Generation](https://arxiv.org/abs/2005.11401) | 参数知识与外部检索结合 |
| [DPR](https://arxiv.org/abs/2004.04906) | 稠密检索和负例训练 |
| [ReAct](https://arxiv.org/abs/2210.03629) | 交替推理与行动 |
| [Chain-of-Thought Prompting](https://arxiv.org/abs/2201.11903) | 中间推理示范 |
| [Self-Consistency](https://arxiv.org/abs/2203.11171) | 多路径采样和答案聚合 |
| [HELM](https://arxiv.org/abs/2211.09110) | 多场景、多指标的整体评测 |
| [HumanEval](https://arxiv.org/abs/2107.03374) | 代码任务与 pass@k |
| [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://arxiv.org/abs/2306.05685) | 模型评审与偏差 |
| [RealToxicityPrompts](https://arxiv.org/abs/2009.11462) | 训练数据及生成可靠性风险 |

## 官方文档

| 文档 | 核对事项 |
| --- | --- |
| [PyTorch CrossEntropyLoss](https://docs.pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html) | logits、ignore_index、归约与标签形式 |
| [PyTorch SDPA](https://docs.pytorch.org/docs/stable/generated/torch.nn.functional.scaled_dot_product_attention.html) | 张量形状、mask、因果对齐与后端行为 |
| [Hugging Face 分词算法](https://huggingface.co/docs/transformers/tokenizer_summary) | BPE、WordPiece、Unigram 与字节表示 |
| [MCP 架构](https://modelcontextprotocol.io/docs/learn/architecture) | host、client、server 与协议能力 |
| [OWASP LLM 应用风险](https://owasp.org/www-project-top-10-for-large-language-model-applications/) | 提示注入、信息泄漏与工具权限边界 |

面试仓库和教程的组织参考单独记录于 [参考项目与整理依据](reference-projects.md)。
