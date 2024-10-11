"""
动态规划经典问题：爬楼梯问题
假设你正在爬楼梯，需要爬到第 n 阶。每次你可以爬 1 阶或者 2 阶。问有多少种不同的方法可以爬到楼顶？
"""
"""
1. 定义状态
首先，我们需要定义状态。在这个问题中，我们可以将状态定义为到达第 i 阶楼梯的方法数。记为 dp[i]。

2. 状态转移方程
接下来，我们需要找到状态之间的关系，即状态转移方程。对于这个问题，到达第 i 阶楼梯可以从第 i-1 阶爬上来，也可以从第 i-2 阶跨两步上来。
因此，到达第 i 阶的方法数是到达第 i-1 阶和第 i-2 阶方法数的总和。因此，状态转移方程为：
dp[i] = dp[i-1] + dp[i-2]

3. 初始化状态
然后，我们初始化状态。显然，到达第 0 阶只有一种方法（即不爬），到达第 1 阶也只有一种方法（爬一阶）。所以：
dp[0] = 1 和 dp[1] = 1

4. 计算顺序
在这个问题中，我们应该从第 2 阶开始计算，一直计算到第 n 阶。

5. 编写代码
"""

def climb_stairs(n):
    if n <= 1:
        return 1
    dp = (n + 1) * [0]
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


print(climb_stairs(6))


def climb_stairs_optimized(n):
    """
    空间复杂度优化：
    由于每次计算只依赖前两个数（当前台阶的方法数等于前一级台阶方法数+前二级台阶方法数），可以只用两个变量来存储这些值，而不是整个数组。
    这种方法将空间复杂度从 O(n) 降低到 O(1)。
    """
    if n <= 1:
        return 1
    current_stair_ways = previous_stair_ways = previous_previous_stair_ways = 1
    for i in range(2, n+1):
        current_stair_ways = previous_stair_ways + previous_previous_stair_ways
        previous_previous_stair_ways, previous_stair_ways = previous_stair_ways, current_stair_ways

    return current_stair_ways


print(climb_stairs_optimized(6))


