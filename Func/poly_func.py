import random

def polynomial(k: int) -> str:
    x = ''
    for i in range(k,-1,-1):
        if i > 1:
            check_zero = random.randint(0, 100)
            if check_zero == 0:
                x += ''
            else:
                x += f'{check_zero}*x**{i} + '
        elif i == 1:
            check_zero = random.randint(0, 100)
            if check_zero == 0:
                x += ''
            else:
                x +=f'{check_zero}*x + '
        elif i == 0:
            check_zero = random.randint(0,100)
            if check_zero == 0:
                x += '= 0'
            else:
                x += f'{check_zero} = 0'
    r = x.replace('1*','')
    return r

