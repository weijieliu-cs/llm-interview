# 01 数学与机器学习基础

[返回首页](../README.md) · [题目索引](question-bank.md)

## 核心知识

LLM 训练通常把下一个 token 预测看作多分类问题。要能从 logits 到概率、损失、梯度完整解释，也要分清训练误差、泛化误差和任务效果。

对 logits $z\in\mathbb{R}^{V}$，令 $m=\max_i z_i$：

$$
p_i=\frac{e^{z_i-m}}{\sum_j e^{z_j-m}},\qquad
L=-\log p_y,\qquad \frac{\partial L}{\partial z_i}=p_i-\mathbf{1}[i=y].
$$

这里 $V$ 为词表大小，$y$ 是目标类别。梯度公式假设单样本、硬标签、无标签平滑；批次归约会再引入相应缩放。

## 常见面试题

<a id="f01"></a>
### F01｜为什么 Softmax 要减去最大值？【P0】

**回答要点：** 给全部 logits 加减同一个常数不会改变概率，因为分子分母可以约去同一指数因子。减去最大值后最大指数是 1，可避免大正数指数溢出。稳定的交叉熵进一步用 `logsumexp(z) - z[y]` 计算，避免先形成极小概率再取对数。

**追问：** 温度 $T$ 有什么作用？对 $T>0$，使用 $\operatorname{softmax}(z/T)$；温度降低使分布更尖锐，升高使分布更平缓。贪心解码通常作为单独模式实现，不能直接令公式除以 0。

<a id="f02"></a>
### F02｜交叉熵和困惑度是什么关系？【P0】

**回答要点：** 语言模型平均 token 负对数似然为 $\bar L$，以自然对数计算时，困惑度 $\mathrm{PPL}=e^{\bar L}$。它反映模型对目标序列的不确定性，但不直接代表事实准确性或指令遵循能力。跨模型比较应保持分词器、评测文本、上下文策略和有效 token 口径一致。

**追问：** 为什么交叉熵函数通常接收 logits？实现可以融合 LogSoftmax 与负对数似然，提高稳定性；预先 Softmax 会改变函数所解释的输入。参见 [PyTorch CrossEntropyLoss](https://docs.pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html)。

<a id="f03"></a>
### F03｜LayerNorm、RMSNorm 和 BatchNorm 有什么区别？【P0】

**回答要点：** LayerNorm 对每个 token 的特征维度求均值、方差，不依赖批次统计；RMSNorm 用均方根缩放，不做减均值。BatchNorm 常对批次及空间位置统计，训练和推理的统计处理不同。自回归模型通常使用不依赖批次统计的归一化方式，适合不同批量和序列长度。

$$
\mathrm{LN}(x)=\gamma\odot\frac{x-\mu}{\sqrt{\sigma^2+\epsilon}}+\beta,\qquad
\mathrm{RMSNorm}(x)=\gamma\odot\frac{x}{\sqrt{\frac1d\sum_i x_i^2+\epsilon}}.
$$

**追问：** RMSNorm 能否任意替换 LayerNorm？结构和训练分布已变化，通常需要重新训练或适配，不能仅凭计算更少就断言效果等价。

<a id="f04"></a>
### F04｜AdamW 为什么把权重衰减与梯度更新分开？【P1】

**回答要点：** Adam 使用一、二阶矩估计对不同参数自适应缩放梯度。若把 L2 正则直接加到梯度，自适应缩放也会作用于这部分；AdamW 则独立执行权重衰减，使其含义与梯度预条件解耦。学习率、衰减、warmup 和梯度裁剪需要联合考虑。

**追问：** warmup 解决什么问题？训练早期参数与优化器统计尚未稳定，逐步增大学习率有助于降低大更新引起的不稳定；它不能修复错误标签或非法数值。见 [AdamW 原论文](https://arxiv.org/abs/1711.05101)。

<a id="f05"></a>
### F05｜BPE、WordPiece、Unigram 与字节级分词如何比较？【P0】

**回答要点：** BPE 从小单元逐步合并高频相邻单元；WordPiece 用不同的候选选择准则构造子词词表；Unigram 从候选词表出发按概率模型逐步裁剪。字节级描述基础表示单元，可与 BPE 结合，并非与 BPE 互斥。词表大小影响序列长度、嵌入层参数量、多语言覆盖和生成成本。见 [Hugging Face 分词概览](https://huggingface.co/docs/transformers/tokenizer_summary)。

**追问：** 增加专用 token 后要做什么？调整嵌入与输出层尺寸，确认新增参数可训练、序列化正常，并验证旧能力；不要假设所有模型都绑定输入输出权重。

<a id="f06"></a>
### F06｜训练损失持续下降但验证效果变差，如何分析？【P0】

**回答要点：** 先确认训练和验证损失使用相同掩码、归约及数据处理。再检查过拟合、训练验证分布差异、标注噪声、模板变化和生成配置。对照任务指标与通用能力，使用早停、数据清洗、降低训练强度或回放数据，并通过对照实验确认原因。

**追问：** 增大 batch 是否等价于增加梯度累积？仅在损失归约、随机性和更新节奏等条件一致时近似等价；见 [分布式训练 D04](06-distributed-training.md#d04)。

## 易错点

- 把 token、汉字、单词当作一一对应的单位。
- 比较不同分词器下的 PPL，却忽略预测事件本身已不同。
- 将归一化层位置、归一化算法和正则化混为一谈。

下一章：[Transformer 与模型结构](02-transformer.md)。
