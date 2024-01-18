def range_parser(s):
    s = s.replace(' ', '')
    tokens = s.split(',')
    l = []
    for t in tokens:
        if t.find('-') != -1:
            if t.find(':') != -1:
                for i in range(  int( t[:t.find('-')] ),  int( t[t.find('-') + 1:t.find(':')] ) + 1,  int( t[t.find(':') + 1:] )   ):
                    l.append(i)
            else:
                for i in range(  int(t[:t.find('-')]),  int(t[t.find('-') + 1:]) + 1 ):
                    l.append(i)
        else:
            l.append(int(t))
    return l