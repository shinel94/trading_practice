def pb3_1():
    naver_closing_price = []
    naver_closing_price.append(474500)
    naver_closing_price.append(461500)
    naver_closing_price.append(501000)
    naver_closing_price.append(500500)
    naver_closing_price.append(488500)
    return naver_closing_price


def pb3_2():
    naver_closing_price = pb3_1()
    print(max(naver_closing_price))
    return max(naver_closing_price)


def pb3_3():
    naver_closing_price = pb3_1()
    print(min(naver_closing_price))
    return min(naver_closing_price)


def pb3_4():
    print(pb3_2() - pb3_3())
    return None


def pb3_5():
    print(pb3_1()[2])
    return None


def pb3_6():
    naver_closing_price2 = dict()
    for idx, price in enumerate(pb3_1()):
        key = '09' + '/' + f'{idx+7}'.zfill(2)
        naver_closing_price2[key] = price
    return naver_closing_price2


def pb3_7():
    naver_closing_price2 = pb3_6()
    print(naver_closing_price2['09/09'])


if __name__ == '__main__':
    print(pb3_1())
    pb3_2()
    pb3_3()
    pb3_4()
    pb3_5()
    print(pb3_6())
    pb3_7()