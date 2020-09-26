def pb4_1():
    for _ in range(5):
        print('*', end='')

def pb4_2():
    print('')
    for _ in range(4):
        pb4_1()
        print('')

def pb4_3():
    for i in range(5):
        for j in range(i+1):
            print('*', end='')
        print('')


def pb4_4():
    for i in range(5):
        for j in range(5-i):
            print('*', end='')
        print('')

def pb4_5():
    for i in range(5):
        result = ' '*(5 - i - 1) + '*'*(i+1)
        print(result)


def pb4_6():
    for i in range(4, -1, -1):
        result = ' '*(5 - i - 1) + '*'*(i+1)
        print(result)

def pb4_7():
    for i in range(5):
        result = ' '*(5 - i - 1) + '*'*(2*i+1) + ' '*(5 - i - 1)
        print(result)


def pb4_8():
    for i in range(4, -1, -1):
        result = ' '*(5 - i - 1) + '*'*(2*i+1) + ' '*(5 - i - 1)
        print(result)

if __name__ == '__main__':
    pb4_1()
    pb4_2()
    pb4_3()
    pb4_4()
    pb4_5()
    pb4_6()
    pb4_7()
    pb4_8()