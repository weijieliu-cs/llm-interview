# 公式与易错点速查

[返回首页](../README.md) · [知识点导航](knowledge-map.md)

## 核心公式

| 知识点 | 公式 | 条件与入口 |
| --- | --- | --- |
| Softmax 交叉熵梯度 | $\partial L/\partial z_i=p_i-\mathbf1[i=y]$ | 单样本硬标签，无平滑；[F01](01-fundamentals.md#f01) |
| 困惑度 | $\mathrm{PPL}=e^{\bar L}$ | 自然对数、有效 token 平均；[F02](01-fundamentals.md#f02) |
| Attention | $\mathrm{softmax}(QK^T/\sqrt{d_h}+M)V$ | 明确形状与 mask；[T01](02-transformer.md#t01) |
| LoRA 参数量 | $r(d_{in}+d_{out})$ | 单矩阵，不含额外 bias 等；[S03](04-finetuning.md#s03) |
| DPO | $-\log\sigma(\beta\Delta)$ | $\Delta$ 是 chosen/rejected 相对参考策略的对数概率差；[A02](05-alignment.md#a02) |
| 训练 FLOPs 估算 | $C\approx6ND$ | 稠密模型近似，不覆盖全部开销；[P03](03-pretraining.md#p03) |
| KV 缓存 | $2LBSH_{kv}d_hb$ | 各层同维、无压缩分片；[I02](07-inference.md#i02) |
| Recall@k | $|G\cap R_k|/|G|$ | 去重命中，明确空标签处理；[E02](09-evaluation.md#e02) |
| 平均在途请求 | $\bar N=\lambda\bar W$ | 稳定系统、均值口径；[X03](10-system-design.md#x03) |

## 两个估算例子

**训练状态：** 假设低精度权重与梯度、FP32 主权重和 Adam 一二阶矩，合计约 16 bytes/参数。7B 参数约为 112 GB / 104.3 GiB，未包括激活、通信和临时缓冲。

**KV Cache：** 32 层、1 条 4096 token 序列、8 个 KV 头、单头 128 维、每元素 2 bytes，合计 512 MiB。批量、长度和 KV 头数变化会线性影响该理论体积。

## 快速辨析

- loss mask 控制监督位置；attention mask 控制可见输入，二者独立。
- GQA 减少 K/V 头数；FlashAttention 优化注意力 IO；PagedAttention 管理 KV 存储。
- LoRA 降低可训练参数量；QLoRA 还压缩冻结基座，仍需激活与计算。
- DPO 使用静态偏好对；经典 PPO/GRPO 还涉及策略采样，版本细节需核对。
- Hit@k 看是否命中；Recall@k 看相关证据覆盖；MRR 看首个命中的排序。
- 更多采样提高候选覆盖不等于系统能选出正确答案。
- 模型生成工具参数后，应用仍要执行校验、授权和错误处理。
- 公开榜单、训练奖励与业务成功率是不同评测对象。

完整推导和资料位于各题及 [参考资料](references.md)。
