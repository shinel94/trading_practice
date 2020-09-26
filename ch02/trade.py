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


if __name__ == '__main__':
    value_check(590000, 610000, 0.05)
    value_check(570000, 610000, 0.05)