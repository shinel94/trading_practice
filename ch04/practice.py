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


def pb4_9():
    apart = [[101, 102, 103, 104], [201, 202, 203, 204], [301, 302, 303, 304], [401, 402, 403, 404]]
    arrears = [101, 203, 301, 404]
    for apart_floor in apart:
        for room in apart_floor:
            if room in arrears:
                print(f'{room}은 구독료가 미납되어 신문이 배달되지 않습니다.')
            else:
                print(f'{room} 신문 배달 완료')

if __name__ == '__main__':
    pb4_1()
    pb4_2()
    pb4_3()
    pb4_4()
    pb4_5()
    pb4_6()
    pb4_7()
    pb4_8()
    pb4_9()