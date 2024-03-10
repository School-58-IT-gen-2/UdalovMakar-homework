def scramble(s1, s2):
    return all(list([s1.count(x) >= s2.count(x) for x in s2]))

print(scramble("tmsnbmbwjqjx", "wjbqtmjsq"))