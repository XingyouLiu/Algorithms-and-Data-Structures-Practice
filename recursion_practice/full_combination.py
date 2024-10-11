def full_combination(numbers, start = None, one_combination = None, combinations = None):
    if one_combination == None:
        one_combination = []
    if combinations == None:
        combinations = []
    if start == None:
        start = 0

    combinations.append(one_combination.copy())

    for i in range(start, len(numbers)):
        one_combination.append(numbers[i])
        full_combination(numbers, i + 1, one_combination, combinations)
        one_combination.pop()

    return combinations


print(full_combination([2,5,1,3]))

"""
1:
combinations = [[]]
start = 0
for i in range(0, 4): i=0, one_combination = [2]
2:
combinations = [[], [2]]
start = 1
for i in range(1, 4): i=1, one_combination = [2, 5]
3:
combinations = [[], [2], [2,5]]
start = 2
for i in range(2, 4): i=2, one_combination = [2,5,1]
4:
combinations = [[], [2], [2,5], [2,5,1]]
start = 3
for i in range(3, 4): i=3, one_combination = [2,5,1,3]
5:
combinations = [[[], [2], [2,5], [2,5,1], [2,5,1,3]]
start = 4
for i in range(4,4): return to 4 and continue
4:
one_combination = [2,5,1]
return to 3 and continue
3:
one_combination = [2,5]
i=3, one_combination = [2,5,3]
3-1:
combinations = [[[], [2], [2,5], [2,5,1], [2,5,1,3], [2,5,3]]
start = 4
for for i in range(4, 4): return to 3 and continue
3:
one_combination = [2,5]
return to 2 and continue
2:
one_combination [2]
i=2, one_combination = [2,1]
2-1:
combinations = [[[], [2], [2,5], [2,5,1], [2,5,1,3], [2,5,3], [2,1]]
start = 3
for i in range(3,4): i=3, one_combination = [2,1,3]
2-1-1:
combinations = [[[], [2], [2,5], [2,5,1], [2,5,1,3], [2,5,3], [2,1], [2,1,3]]
start = 4
for i in range(4,4): return to 2-1 and continue
2-1:
one_combination = [2,1]
return to 2 and continue
2:
one_combination = [2]
i=3, one_combination = [2,3]
2-1':
start = 4
for i in range(4,4): return to 2 and continue
2:
one_combination = [2]
return to 1 and continue
1:
one_combination = []
i = 1, one_combination = [5]
1-1:
start = 2
combinations = combinations = [[[], [2], [2,5], [2,5,1], [2,5,1,3], [2,5,3], [2,1], [2,1,3],[2,1,5], [5]]
.............

"""

