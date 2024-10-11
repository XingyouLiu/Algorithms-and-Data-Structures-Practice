def longest_increasing_subsequence(array):
    """
    dp[i]表示的是在数组 array[0] 到 array[i]（包含 array[i]）的部分中找到的最长递增子序列的长度, 即数组前 i+1 个元素中，可以找到的最长递增子序列的长度。
    """
    longest_length = 1
    dp = len(array) * [1]
    for i in range(1, len(array)):
        for j in range(i):
            if array[j] < array[i]:
                dp[i] = max(dp[i], dp[j] + 1)
        longest_length = max(longest_length, dp[i])

    return longest_length


print(longest_increasing_subsequence([5,3,1,0,2,-1,3,-2,4,-3,-10,5,6,-7]))



"""
以下是寻找最长、递增、连续的子序列的代码！
如果是寻找最长递增子序列，子序列不需要是连续的！！！
"""
def longest_continuous_increase_subsequence(array):
    longest_length = 1
    subsequence_first_num = array[0]
    subsequence_first_index = 0
    for i in range(1, len(array)):
        if array[i] <= array[i - 1]:
            subsequence_first_num = array[i]
            subsequence_first_index = i

        if i < len(array) - 1:
            if array[i + 1] <= array[i]:
                subsequence_length = i - subsequence_first_index + 1
                longest_length = max(longest_length, subsequence_length)
        else:
            subsequence_length = i - subsequence_first_index + 1
            longest_length = max(longest_length, subsequence_length)

        if subsequence_first_num > array[i]:
            subsequence_first_num = array[i]
            subsequence_first_index = i


    return longest_length


print(longest_continuous_increase_subsequence([3,5,1,2,3,4,10,-10,1,2,3,4,5,6,-1,-3]))