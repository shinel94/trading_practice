from crawler.crawler import BaseCrawler


class NaverCrawler(BaseCrawler):
    def __init__(self):
        super(BaseCrawler, self).__init__()

    def _crawl(self, page_data):
        result = dict()
        result.update(self.__get_name(page_data))
        result.update(self.__get_price(page_data))
        return result

    @staticmethod
    def __get_name(page_data):
        name = page_data[4].columns[1].split('*')[0]
        code = page_data[4].columns[1].split('*')[1]
        return {'name': name,
                'code': code}

    @staticmethod
    def __get_price(page_data):
        price = page_data[4].loc[0][1]
        price_change = page_data[4].loc[1][1].split('  ')
        change = ''
        for val in price_change[1].split(','):
            change += val
        change = int(change)
        if price_change[0] == '하향':
            change = -change
        profit = page_data[4].loc[7][1]
        eps = page_data[4].loc[10][1]
        per = page_data[4].loc[12][1]
        pbr = page_data[4].loc[13][1]
        industry_per = dict()
        industry_per['mean'] = page_data[9][1][0].split('배')[0]
        industry_per['max'] = page_data[9][1][0].split('배')[0]
        industry_per['min'] = page_data[9][1][0].split('배')[0]
        nearest_month = page_data[3].columns[-1][1]
        if '(E)' in nearest_month:
            nearest_month = page_data[3].columns[-2][1]

        # TODO : bps, pbr, gp_a 상세 구현 필요
        return {
            'price': price,
            'per': per,
            'eps': eps,
            'industry_per_static': industry_per,
            'nearest_month': nearest_month,
            'bps': None,
            'pbr': None,
            'gp_a': None
        }

