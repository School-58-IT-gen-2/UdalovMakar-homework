def score(dice):
    score = 0
    for i in range(1, 7):
        count_ = dice.count(i)
        if count_ > 2:
            score += 1000 if i == 1 else i * 100
            count_ -= 3
        if i == 1 or i == 5:
            score += 50 * count_ if i == 5 else 100 * count_
    return score