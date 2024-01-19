def increment_string(strng: str):
    if strng == '': return '1'
    if strng[-1].isalpha(): return strng + '1'
    if strng[-1] == '0': return strng[:-1] + '1'
    numb_s = ''
    for i in range(len(strng)-1, -1, -1):
        i = strng[i]
        if i.isalpha() or i == '0':
            if numb_s == '9' * len(numb_s) and i == '0': strng = strng[:-1]
            break
        else:
            numb_s += i
            strng = strng[:-1]
    numb = int(numb_s[::-1])
    return strng + str(numb + 1)