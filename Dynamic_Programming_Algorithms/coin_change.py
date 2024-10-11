"""
在这个问题中，我们可以使用动态规划来找出每个金额所需的最少硬币数量。我们可以定义一个数组 dp，其中 dp[i] 表示组成金额 i 所需的最少硬币数量。

状态定义
dp[i] 表示组成金额 i 所需的最少硬币数量。
状态转移方程
dp[i] = min(dp[i], dp[i - coin] + 1) (对于所有的 coin 在 coins 中)。

初始化
初始化 dp[0] = 0，因为组成金额 0 所需的硬币数量为 0。
对于其他的 i，可以初始化为一个大数（例如 amount + 1），表示初始时无法用硬币组成这个金额。
计算顺序
从 dp[1] 到 dp[amount] 依次计算。
算法步骤
初始化一个长度为 amount + 1 的数组 dp，所有值设为 amount + 1。
将 dp[0] 设为 0。
遍历金额从 1 到 amount。
对于每个金额 i，遍历每个硬币 coin。如果 coin <= i，则更新 dp[i]。
最后，检查 dp[amount] 是否被更新，如果是，则返回 dp[amount]，否则返回 -1。
"""

def coin_change(coins, amount):
    dp = (amount + 1) * [amount + 1]
    dp[0] = 0
    for i in range(1, len(dp)):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != amount + 1 else -1


print(coin_change([1, 2, 5, 10], 37))
