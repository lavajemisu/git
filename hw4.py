def Wellcome(name):
    n = name
    return

def rep_char(c,n):
    
    print(c * n)

def draw_line_string(msg1,msg2):
    nstr = len(msg1)if(len(msg1)>len(msg2))else len(msg2)
    rep_char('-', nstr * 1)
    print(f'{msg1}')
    print(f'{msg2}')
    rep_char('-', nstr * 1)


n = input('input his/her name: ')



draw_line_string(f' Hello {n}, ',' Wellcome to Seoul. ')


