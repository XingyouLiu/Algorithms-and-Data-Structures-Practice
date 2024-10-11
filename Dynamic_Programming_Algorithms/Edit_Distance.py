def edit_distance(str1, str2):
    n = len(str1)
    m = len(str2)
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(n + 1): #初始化了dp数组的第一行，第一行中每一列的值分别代表从空字符串到 str1 的前 i 个字符的编辑距离。
        dp[i][0] = i
    for j in range(1, m + 1): #初始化了dp数组的第一列，第一列中每一行的值分别代表从空字符串到 str2 的前 j 个字符的编辑距离。
        dp[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] != str2[j - 1]:
                dp[i][j] = min(dp[i - 1][j - 1] + 1, dp[i - 1][j] + 1, dp[i][j - 1] + 1) #如果字符不匹配，选择插入、删除或替换操作中的最小代价
            else:
                dp[i][j] = dp[i - 1][j - 1] #如果字符匹配，沿用之前的编辑距离

    return dp[n][m]


print(edit_distance('standing', 'sitting'))