def make_readable(seconds):
    h = seconds // 3600
    m = seconds % 3600 // 60
    s = seconds % 3600 % 60
    return f'{"0" * (2 - len(str(h)))}{h}:{"0" * (2 - len(str(m)))}{m}:{"0" * (2 - len(str(s)))}{s}'
