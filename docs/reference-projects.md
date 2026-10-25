# 参考项目与整理依据

[返回首页](../README.md) · [知识点导航](knowledge-map.md)

本项目在 **2026-10-25** 查看下列仓库的 README 和目录，以确定知识覆盖与组织方式。这里记录的是参考依据，不代表逐题验证了它们的全部答案，也不把它们标为公司官方题库。

| 参考项目 | 查看入口 | 借鉴的组织方式 | 本项目的对应内容 |
| --- | --- | --- | --- |
| [wdndev/llm_interview_note](https://github.com/wdndev/llm_interview_note) | [README](https://github.com/wdndev/llm_interview_note/blob/main/README.md) | 基础、结构、数据、分布式、SFT、推理、强化学习、RAG、评测、应用的主题划分 | 01—09 主干章节及 11、12 补充专题 |
| [km1994/LLMs_interview_notes](https://github.com/km1994/LLMs_interview_notes) | [README](https://github.com/km1994/LLMs_interview_notes/blob/main/README.md) | 位置编码、Tokenizer、PEFT、KV Cache、幻觉等细分考点与问答导航 | 显式题号、回答要点、追问及知识点交叉索引 |
| [datawhalechina/llm-universe](https://github.com/datawhalechina/llm-universe) | [README](https://github.com/datawhalechina/llm-universe/blob/main/README.md)、[docs](https://github.com/datawhalechina/llm-universe/tree/main/docs) | 文档处理、知识库、检索生成、验证迭代的实践路径 | RAG 分层诊断、项目实验模板、检索指标练习 |

## 分类如何落地

- **基础与结构：** 将数学、分词、Transformer、经典 NLP 和 Embedding 分开定位，用链接连接交叉知识点。
- **训练链路：** 区分预训练及数据、SFT/PEFT、偏好对齐、分布式与显存，不将所有训练问题塞入“微调”。
- **推理与应用：** 推理性能、RAG/Agent、提示词与上下文各有入口，便于按算法、应用、Infra 岗位复习。
- **评测与面试：** 所有方向共用评测口径、场景设计、项目举证与代码练习。

正文和示例按上述主题独立编写，技术判断优先回到 [论文与官方资料](references.md)。本次未导入参考仓库的正文、图片、代码或付费答案。

## 后续收录面经的规则

面经记录至少包含公开来源链接、发布日期或访问日期、岗位方向、原始问题与知识点映射。公司、轮次和时间缺失时标为“未注明”；未经核实的转载标为“待核实”。删去个人信息，概括问题并回链来源，避免整篇复制。

当前 72 道题是按知识点整理的练习题，**不声称为已核实的某公司真题**。个人复盘可使用 [面经记录模板](interview-practice.md#experience-template)。
