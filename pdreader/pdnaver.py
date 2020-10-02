from util.singleton import Singleton
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
from VO.stock import Stock
from crawler.naver import NaverCrawler


class PDNaver(Singleton):
    def __init__(self):
        self.__stock_chart_url = 'http://finance.naver.com/item/sise_day.nhn?code='
        self.__stock_info_url = 'https://finance.naver.com/item/main.nhn?code='
        self.naver_page_crawler = NaverCrawler()

    def get_chart_by_code(self, code):
        df = pd.DataFrame()
        for page in range(1, 21):
            pg_url = f'{self.__stock_chart_url}{code}&page={page}'
            df = df.append(pd.read_html(pg_url, header=0)[0], ignore_index=True)
        df = df.dropna()
        df = df.rename(columns={'날짜': 'date', '종가': 'close', '전일비': 'diff', '시가': 'open', '고가': 'high', '저가': 'low',
                                '거래량': 'volume'})
        df['date'] = pd.to_datetime(df['date'])
        df = df.sort_values(by=['date'], ascending=True)

        return df

    def get_trading_amount_by_code(self, code, period=60):
        df = self.get_chart_by_code(code)
        target = np.asarray(df['volume'].astype(int))
        target = target[-period:]
        target = np.asarray(target)
        if len(target) == 0:
            return 0
        averageVolume = (np.sum(target) - target[-1]) / (target.shape[0] - 1)
        return averageVolume

    def get_beta_by_code(self, code):
        df = self.get_chart_by_code(code)
        target = np.asarray(df['close'].astype(int))
        x = np.arange(0, target.shape[0])
        model = LinearRegression()
        model.fit(x[..., np.newaxis], target)
        return model.coef_[0]

    def get_stock_info_by_code(self, code):
        pg_url = f'{self.__stock_info_url}{code}'
        page_data = pd.read_html(pg_url, encoding='euc-kr')
        trading_amount_ratio = self.get_trading_amount_by_code(code)
        beta = self.get_beta_by_code(code)
        return Stock(**self.naver_page_crawler.crawl(page_data), industry_code=None, beta=beta, trading_amount_ratio=trading_amount_ratio)


if __name__ == '__main__':
    pd_naver = PDNaver()
    # beta = pd_naver.get_beta_by_code('016380')
    beta = pd_naver.get_stock_info_by_code('016380')
    print(beta)