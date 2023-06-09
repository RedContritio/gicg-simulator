# 用强化学习和监督学习技术来玩炉石

Mishchenko, Y., & Lanctot, M. (2018). Applying Machine Learning to Hearthstone with TensorFlow. arXiv preprint arXiv:1805.00733.

## 不同 agent 类型

该论文提出了四种不同类型的 agent 来玩《炉石传说》。这些 agent 是：

1. 随机 agent ：该 agent 无需任何策略或决策过程即可随机选择动作。它被用作与其他 agent 进行比较的基准。

2. 基于规则的 agent ：此 agent 使用一组预定义的规则来选择操作。这些规则以专家知识和经验为基础。 agent 旨在模仿人类玩家的决策过程。

3. 强化学习 agent ：该 agent 使用强化学习来学习选择动作的最佳策略。 agent 通过反复试验来学习，其政策会根据游戏期间获得的奖励进行更新。

4. 混合 agent ：该 agent 结合了基于规则的学习方法和强化学习方法。 agent 使用预定义的规则在某些情况下选择操作，并在其他情况下使用强化学习来学习最佳策略。

该论文使用一系列实验评估了这些 agent 的性能。结果表明，混合 agent 的表现优于其他 agent ，并且能够与游戏专家竞争。

## Treewalking 搜索动作顺序

Treewalking 算法是论文中提出的一种搜索算法，用于确定《炉石传说》中给定回合的最佳动作顺序。该算法的工作原理是探索游戏树并评估搜索过程中遇到的每种游戏状态的质量。该算法使用游戏状态指标，该函数将游戏状态映射到代表状态质量的实数。该指标用于指导搜索以采取更好的行动。

Treewalking 算法包括以下步骤：

1. 通过将当前游戏状态设置为游戏的初始状态来初始化搜索；
2. 生成可以从当前游戏状态执行的所有可能动作；
3. 使用游戏状态指标评估每种生成的游戏状态的质量；
4. 选择能带来最高质量游戏状态的动作；
5. 将当前游戏状态更新为选定的游戏状态；
6. 重复步骤 2-5 直到回合结束。

该算法使用深度优先搜索策略来探索游戏树。但是，搜索受游戏状态指标的指导，这使算法能够专注于最有前途的游戏状态。游戏状态指标是使用监督学习技术学习的，这涉及在游戏状态及其相应的质量分数数据集上训练模型。

Treewalking 算法比《炉石传说》中以前使用的搜索算法有所改进，因为它降低了问题的计算复杂性，并且使得在合理的时间内搜索最佳动作序列变得可行。该算法是使用四种不同的 agent 进行评估的，与以前的研究相比，其中两个显示出更好的结果。最优的 agent 能够与游戏专家竞争。

## 特征设计

### 1.选择相关的游戏状态变量

选择相关游戏状态变量的过程涉及识别对代理决策过程至关重要的变量。就炉石传说而言，相关的游戏状态变量包括：

1. 玩家和对手的生命值：决定游戏的结果。代理人在选择动作时需要考虑两个玩家的生命值。
2. 玩家手中的牌数：决定玩家可用的选项。代理人在选择动作时需要考虑玩家手中的卡牌数量。
3. 棋盘上的小兵数量：决定棋盘状态。特工在选择动作时需要考虑棋盘上小兵的数量。
4. 玩家可用的法力值：决定玩家可用的资源。代理在选择动作时需要考虑玩家可用的法力值。
5. 玩家牌组中的卡牌类型：决定玩家在未来回合中可用的选项。代理人在选择动作时需要考虑玩家牌组中的卡牌类型。

### 2. 将变量转换成特征

将变量转换为特征所涉及的步骤如下：

1. 选择相关的游戏状态变量：这些变量包括玩家和对手的生命值、玩家手中的卡牌数量、棋盘上的小兵数量以及玩家可用的法力值。
2. 标准化：将变量标准化为通用尺度。这涉及将变量缩放到 0 到 1 的范围内，其中 0 表示变量的最小值，1 表示变量的最大值。
3. 离散化：将变量离散化为一组离散值。这包括将变量的范围划分为一组间隔，并为每个间隔分配一个离散值。此步骤适用于魔法值和生命值等变量，它们的值范围有限。
4. one-hot 编码：将 one-hot 编码应用于类别变量，例如卡片类型。这涉及为每个类别创建一个二进制向量，其中该类别的向量值为 1，所有其他类别的向量值为 0。
5. 创建特征向量：创建一个将所有变换后的变量组合在一起的特征向量。这涉及将归一化、离散化和 onehot 编码的变量连接成单个特征向量，该向量可用作强化学习算法的输入。

特征的设计是强化学习过程的一个重要方面，因为它决定了算法输入的质量及其学习最优策略的能力。设计过程是迭代式的，包括试验不同的功能集并评估它们对代理性能的影响。
