from cybos.cybos import CybosTrader


def main():

    trader = CybosTrader()
    trader.reserve_buy_stock_best('A001500', 4000)
    # trader.buy_stock_designation('A001500', 4000, 10100)

if __name__ == '__main__':
    main()