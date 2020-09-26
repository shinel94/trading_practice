def sell_stock():
    pass

def contain_stock():
    pass

def value_check(now_value, original_value, rate_lower_bound):
    if now_value < (original_value * (1 - rate_lower_bound)):
        print('전량 매도')
        sell_stock()
    else:
        print('보유')
        contain_stock()


def tot_stock(stock_per_value, stock_num):
    return stock_num * stock_per_value


def pb2_1():
    daum = 89000
    naver = 751000
    daum_stock = 100
    naver_stock = 20
    daum_value = tot_stock(daum, daum_stock)
    naver_value = tot_stock(naver, naver_stock)
    tot = daum_value + naver_value
    return tot

def pb2_2():
    daum = 89000
    naver = 751000
    daum_stock = 100
    naver_stock = 20
    daum_value = tot_stock(daum, daum_stock)
    naver_value = tot_stock(naver, naver_stock)
    tot = daum_value + naver_value
    daum_value = tot_stock(daum*0.95, daum_stock)
    naver_value = tot_stock(naver*0.9, naver_stock)
    tot_after = daum_value + naver_value
    loss = tot - tot_after
    return loss


def pb2_3(F):
    return (F-32)/1.8


def pb2_4():
    repeat_word = 'pizza'
    result = repeat_word + '\n'
    result = result*10
    return result


def pb2_5(count):
    start_stock = 1000000
    last_stock = start_stock * (0.7**count)
    return last_stock


def pb2_6(name, birth, id_number):
    result = f'이름: {name} 생년월일: {birth.year}년 {birth.month}월 {birth.day}일 주민등록번호: {id_number}'
    return result

def pb2_7():
    inputs = 'Daum KaKao'
    temp = inputs.split(' ')
    result = temp[1] + ' ' + temp[0]
    return result


def pb2_8():
    inputs = 'hello world'
    temp = inputs.split(' ')
    temp[0] = 'hi'
    result = ' '.join(temp)
    return result

def pb2_9():
    inputs = 'abcdef'
    result = inputs[1:] + inputs[0:1]
    return result

if __name__ == '__main__':
    import datetime
    value_check(590000, 610000, 0.05)
    value_check(570000, 610000, 0.05)
    monday_closing_price = 10000 * 0.7
    tuesday_closing_price = monday_closing_price * 0.7
    print(f'화요일 종가 : {tuesday_closing_price}')
    print(pb2_1())
    print(pb2_2())
    print(pb2_3(50))
    print(pb2_4())
    print(pb2_5(3))
    print(pb2_6('파이썬', datetime.datetime.today(), '20141212-1623210'))
    print(pb2_7())
    print(pb2_8())
    print(pb2_9())