def zero(func=None): 
    if func: return eval('0' + func)
    else: return 0
def one(func=None): 
    if func: return eval('1' + func)
    else: return 1
def two(func=None): 
    if func: return eval('2' + func)
    else: return 2
def three(func=None): 
    if func: return eval('3' + func)
    else: return 3
def four(func=None): 
    if func: return eval('4' + func)
    else: return 4
def five(func=None): 
    if func: return eval('5' + func)
    else: return 5
def six(func=None): 
    if func: return eval('6' + func)
    else: return 6
def seven(func=None): 
    if func: return eval('7' + func)
    else: return 7
def eight(func=None): 
    if func: return eval('8' + func)
    else: return 8
def nine(func=None): 
    if func: return eval('9' + func)
    else: return 9

def plus(num):
    return f' + {str(num)}'
def minus(num):
    return f' - {str(num)}'
def times(num):
    return f' * {str(num)}'
def divided_by(num):
    return f' // {str(num)}'

print(nine(divided_by(two())))