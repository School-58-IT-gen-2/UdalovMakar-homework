def beeramid(bonus, price):
    count_ = bonus // price
    count_in_beeramid = 0
    n = 0
    while count_in_beeramid <= count_:
        n += 1
        count_in_beeramid += n ** 2
    if n < 1: return 0
    return n - 1

print(beeramid(1500, 2))