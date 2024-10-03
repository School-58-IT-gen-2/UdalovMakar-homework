def format_duration(seconds):
    if seconds == 0: return 'now'
    y = seconds // 31536000
    d = seconds % 31536000 // 86400
    h = seconds % 31536000 % 86400 // 3600
    m = seconds % 31536000 % 86400 % 3600 // 60
    s = seconds % 31536000 % 86400 % 3600 % 60
    y_ = 'year' if y == 1 else 'years'
    d_ = 'day' if d == 1 else 'days'
    h_ = 'hour' if h == 1 else 'hours'
    m_ = 'minute' if m == 1 else 'minutes'
    s_ = 'second' if s == 1 else 'seconds'
    strs = list(filter(lambda x: x != None, 
            [str(y) + ' ' + y_ if y > 0 else None,
            str(d) + ' ' + d_ if d > 0 else None,
            str(h) + ' ' + h_ if h > 0 else None,
            str(m) + ' ' + m_ if m > 0 else None,
            str(s) + ' ' + s_ if s > 0 else None]))
    return strs[0] if len(strs) == 1 else ', '.join(strs[:-1]) + f' and {strs[-1]}'
