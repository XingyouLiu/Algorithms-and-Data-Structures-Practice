class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz',
        }

        n = len(digits)
        if n == 0:
            return []

        def solution1(i, ans, combination):
            if ans == None:
                ans = []
            if combination == None:
                combination = ''

            if i == n:
                ans.append(combination)
                return
            str = dic[int(digits[i])]
            for c in str:
                combination += c
                solution1(i + 1, ans, combination)
                combination = combination[:-1]

            return ans

        return solution1(0, None, None)

        def solution(i, j, ans, combination):
            if ans == None:
                ans = []
            if combination == None:
                combination = ''
            if i == n:
                ans.append(combination)
                return
            str = dic[int(digits[i])]
            m = len(str)
            if j == m:
                return
            combination += str[j]
            solution(i + 1, 0, ans, combination)
            combination = combination[:-1]
            solution(i, j + 1, ans, combination)

            return ans

        return solution(0, 0, None, None)