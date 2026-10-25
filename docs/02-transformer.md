# 02 Transformer 与模型结构

[返回首页](../README.md) · [题目索引](question-bank.md)

## 核心知识

设 batch 为 $B$、序列长度为 $S$、隐藏维度为 $d$、查询头数为 $H_q$、单头维度为 $d_h$。常见结构中 $d=H_qd_h$，每头计算：

$$
\operatorname{Attention}(Q,K,V)=\operatorname{softmax}\left(\frac{QK^\top}{\sqrt{d_h}}+M\right)V.
$$

$Q$ 的形状为 $[B,H_q,S_q,d_h]$，单头分数矩阵为 $[S_q,S_k]$。$M$ 对允许位置取 0、屏蔽位置取负无穷。自回归训练同时计算多个位置，但使用因果掩码阻止读取未来 token。原始结构见 [Attention Is All You Need](https://arxiv.org/abs/1706.03762)。

## 常见面试题

<a id="t01"></a>
### T01｜Attention 为什么除以根号下的单头维度？【P0】

**回答要点：** 若 $q_i,k_i$ 相互独立、均值为 0、方差为 1，点积 $\sum_iq_ik_i$ 的方差随 $d_h$ 线性增大。除以 $\sqrt{d_h}$ 将其缩放到相对稳定的范围，避免 Softmax 过早饱和。这是基于简化统计假设的解释，不意味着实际训练特征严格满足独立同分布。

**追问：** 标准全注意力的复杂度是什么？分数与加权求和约为 $O(BHS^2d_h)$；显式保存分数矩阵需要 $O(BHS^2)$ 空间，还需计入投影和激活。

<a id="t02"></a>
### T02｜Pre-Norm 与 Post-Norm 如何比较？【P0】

**回答要点：** Pre-Norm 的子层可写成 $x+f(\mathrm{Norm}(x))$，Post-Norm 写成 $\mathrm{Norm}(x+f(x))$。Pre-Norm 保留更直接的残差梯度路径，通常有利于深层训练稳定；效果也依赖初始化、学习率和最终归一化。不能仅凭一种排列断言所有任务更好。参见 [On Layer Normalization in the Transformer Architecture](https://arxiv.org/abs/2002.04745)。

**追问：** FFN 的作用是什么？Attention 混合位置间信息，FFN 在各位置独立做非线性特征变换。门控 FFN 如 SwiGLU 会改变投影个数和中间维度，需要按实际结构估算参数。

<a id="t03"></a>
### T03｜RoPE 为什么能体现相对位置？【P0】

**回答要点：** RoPE 对 query 和 key 的成对特征施加随位置变化的旋转。利用旋转矩阵性质，可写成 $(R_mq)^\top(R_nk)=q^\top R_{n-m}k$，点积因此依赖相对位置差。它没有自动保证任意长度的外推能力；更长上下文仍需位置缩放、训练和长距离任务评测。参见 [RoFormer](https://arxiv.org/abs/2104.09864)。

**追问：** 增量生成时位置编号如何处理？新 token 必须沿用完整上下文的位置偏移，不能在每次 decode 时重新从 0 计数。

<a id="t04"></a>
### T04｜MHA、MQA、GQA 的差别是什么？【P0】

**回答要点：** MHA 每个查询头对应独立 K/V 头；MQA 所有查询头共享一组 K/V；GQA 让一组查询头共享 K/V，在表示能力和缓存开销之间折中。若 K/V 头数从 $H_q$ 降为 $H_{kv}$，其缓存理论体积按 $H_{kv}/H_q$ 缩放，查询头数保持不变。见 [GQA 原论文](https://arxiv.org/abs/2305.13245)。

**追问：** KV Cache 为什么不保存 Q？后续 token 会产生新的 query，历史 key/value 会被反复读取，历史 query 通常无需重算或保留。

<a id="t05"></a>
### T05｜Encoder、Decoder 和多模态连接结构如何选择？【P1】

**回答要点：** 双向 Encoder 适合表示学习和分类；因果 Decoder 直接建模自回归生成；Encoder-Decoder 将输入编码与输出生成分开，通过交叉注意力连接。多模态模型的一类方案用视觉编码器提取特征，经投影或连接器映射到语言模型表示空间，再进行对齐与指令训练。见 [Visual Instruction Tuning](https://arxiv.org/abs/2304.08485)。

**追问：** 为什么视觉任务要单独评估？图像分辨率、视觉 token 数、OCR 能力、空间关系与图像幻觉无法由纯文本评测覆盖，视觉 token 还会增加上下文和推理成本。

<a id="t06"></a>
### T06｜MoE 为什么参数量大但激活计算量较小？【P1】

**回答要点：** 路由器为每个 token 选择少量专家，常用于替换稠密 FFN。总参数量决定存储等需求，激活专家数量决定部分计算量，两者不能混用。收益受路由均衡、专家容量、跨设备通信和批量大小影响。见 [Switch Transformers](https://arxiv.org/abs/2101.03961)。

**追问：** 主要工程问题有哪些？专家负载不均可能造成热点，跨设备分发带来 all-to-all 通信，容量限制可能导致 token 丢弃或额外调度；需结合具体实现分析。

## 易错点

- 认为因果掩码意味着训练时也必须逐 token 串行。
- 用查询头数代替 KV 头数估算 GQA 缓存。
- 把 MoE 的激活参数量当作全部权重的常驻显存。

动手验证：[因果 Attention 练习](../examples/README.md)。下一章：[预训练与数据](03-pretraining.md)。
