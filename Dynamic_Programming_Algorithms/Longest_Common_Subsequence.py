def longest_common_subsequence(str1, str2):
    """
动态规划解决最长公共子序列问题的思路是逐个比较两个字符串的字符，并利用一个二维数组记录到目前为止的最长公共子序列的长度。
对于字符串 X[1..m] 和 Y[1..n]：
初始化：创建一个 (m+1) x (n+1) 的二维数组 dp。dp[i][j]表示字符串 X[1..i] 和 Y[1..j] 的最长公共子序列的长度。
    """
    n = len(str1)
    m = len(str2)
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

    return dp[n][m]


print(longest_common_subsequence('abcdefg','acfg'))