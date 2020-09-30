class Stock:
    def __init__(self, name, code, fullcode, index, price, per, eps, nearest_month, industry_code, trading_amount_ratio, industry_per_static):
        self.__name = name
        self.__code = code
        self.__fullcode = fullcode
        self.__index = index
        self.__price = price
        self.__per = per
        self.__eps = eps
        self.__nearest_month = nearest_month
        self.__industry_code = industry_code
        self.__trading_amount_ratio = trading_amount_ratio
        self.__industry_per_static = industry_per_static

    @property
    def index(self):
        return self.__index

    @property
    def name(self):
        return self.__name

    @property
    def code(self):
        return self.__code

    @property
    def fullcode(self):
        return self.__fullcode

    @property
    def price(self):
        return self.__price

    @property
    def per(self):
        return self.__per

    @property
    def eps(self):
        return self.__eps

    @property
    def nearest_month(self):
        return self.__nearest_month

    @property
    def industry_code(self):
        return self.__industry_code

    @property
    def trading_amount_ratio(self):
        return self.__trading_amount_ratio

    @property
    def industry_mean_per(self):
        return self.__industry_per_static['mean']

    @property
    def industry_max_per(self):
        return self.__industry_per_static['max']

    @property
    def industry_min_per(self):
        return self.__industry_per_static['min']

    def __repr__(self):
        return str({'index': self.index,
                    'name' : self.name,
                    'code' : self.code,
                    'fullcode': self.fullcode,
                    'price': self.price,
                    'PER': self.per,
                    'EPS': self.eps,
                    'nearest_month': self.nearest_month,
                    'industry_code': self.industry_code,
                    'trading_amount_ratio': self.trading_amount_ratio,
                    'industry_mean_per': self.industry_mean_per,
                    'industry_max_per': self.industry_max_per,
                    'industry_min_per': self.industry_min_per,
                    })
