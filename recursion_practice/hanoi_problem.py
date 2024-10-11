def hanoi(n, start, target, auxiliary):
    if n == 1:
        print(f'Move the disk from {start} to {target}')
    else:
        hanoi(n - 1, start = start, target = auxiliary, auxiliary = target)
        print(f'Move the disk from {start} to {target}')
        hanoi(n - 1, start = auxiliary, target = target, auxiliary = start)


hanoi(4, 'A', 'C', 'B')