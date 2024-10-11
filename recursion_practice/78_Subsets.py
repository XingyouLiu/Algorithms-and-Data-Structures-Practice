class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)

        def subset_help(i, subset, subsets_ans):
            if subset == None:
                subset = []
            if subsets_ans == None:
                subsets_ans = []

            if i == n:
                subsets_ans.append([num for num in subset])
                return
            subset.append(nums[i])
            subset_help(i + 1, subset, subsets_ans)
            subset.pop()
            subset_help(i + 1, subset, subsets_ans)

            return subsets_ans

        return subset_help(0, None, None)

        def subsets_help_1(subset, subsets_ans, start):
            if subset == None:
                subset = []
            if subsets_ans == None:
                subsets_ans = []
            subsets_ans.append([num for num in subset])
            while start < n:
                subset.append(nums[start])
                subsets_help_1(subset, subsets_ans, start + 1)
                subset.pop()
                start += 1

            return subsets_ans

        return subsets_help_1(None, None, 0)

        def help(n):
            if n == 1:
                return [[], [nums[0]]]

            def combine(current_array, num):
                new_current = []
                for arr in current_array:
                    new_current.append(arr)
                    new_current.append(arr + [num])
                return new_current

            return combine(help(n - 1), nums[n - 1])

        return help(n)