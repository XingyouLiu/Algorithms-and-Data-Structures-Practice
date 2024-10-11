class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        def solution1(i, combination, ans, sum_):
            if i > k:
                if sum_ == n:
                    ans.append([num for num in combination])
                return

            for num in nums:
                if combination == [] or combination[-1] < num:
                    combination.append(num)
                    sum_ += num
                    solution1(i + 1, combination, ans, sum_)
                    combination.pop()
                    sum_ -= num

            return ans

        return solution1(1, [], [], 0)

        def solution(i, combination, ans, sum_):
            if combination == None:
                combination = set()
            if ans == None:
                ans = []
            if sum_ == None:
                sum_ = 0

            if i > k:
                if sum_ == n and combination not in ans:
                    ans.append(set(num for num in combination))
                return

            for num in nums:
                if num not in combination:
                    combination.add(num)
                    sum_ += num
                    solution(i + 1, combination, ans, sum_)
                    combination.remove(num)
                    sum_ -= num

            return [list(combination) for combination in ans]

        return solution(1, None, None, None)