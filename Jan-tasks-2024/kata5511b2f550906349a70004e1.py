def last_digit(n1, n2):
    if n2 == 0: return 1
    nums = [
        [1, 1, 1, 1],
        [2, 4, 8, 6],
        [3, 9, 7, 1],
        [4, 6, 4, 6],
        [5, 5, 5, 5],
        [6, 6, 6, 6],
        [7, 9, 3, 1],
        [8, 4, 2, 6],
        [9, 1, 9, 1],
        [0, 0, 0, 0]]
    return nums[int(str(n1)[-1]) - 1][n2 % 4 - 1]