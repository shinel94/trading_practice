from util.singleton import Singleton
import win32com.client as client
from VO.stock import Stock
from VO.chart import Chart
from constant.constant import SECTION_KIND_SHARE, SECTION_KIND_ETN, SECTION_KIND_PRESENT
from constant.constant import STOCKCHART_DAY_CODE, STOCKCHART_OPENING_QUTATION_CODE, STOCKCHART_CLOSING_QUTATION_CODE, STOCKCHART_HIGHEST_QUTATION_CODE, STOCKCHART_LOWEST_QUTATION_CODE, STOCKCHART_TRADING_QUTATION_CODE
from constant.constant import STOCKCHART_CHARTTYPE_DAY_CODE
from constant.constant import MARKETEYE_PRICE_CODE, MARKETEYE_PER_CODE, MARKETEYE_EPS_CODE, MARKETEYE_NEAREST_MONTH_CODE
from constant.constant import TRADE_TYPE_DESIGNATION, TRADE_TYPE_BEST, TRADE_TYPE_FIRST
import numpy as np


class Cybos(Singleton):
    CHART_DATA_TYPE = (
        STOCKCHART_DAY_CODE,
        STOCKCHART_OPENING_QUTATION_CODE,
        STOCKCHART_HIGHEST_QUTATION_CODE,
        STOCKCHART_LOWEST_QUTATION_CODE,
        STOCKCHART_CLOSING_QUTATION_CODE,
        STOCKCHART_TRADING_QUTATION_CODE
    )
    MARKETEYE_TYPE = (
        MARKETEYE_PRICE_CODE,
        MARKETEYE_PER_CODE,
        MARKETEYE_EPS_CODE,
        MARKETEYE_NEAREST_MONTH_CODE
    )
    def __init__(self):
        self.__cybos = client.Dispatch('CpUtil.CpCybos')
        self.__stockcode = client.Dispatch('CpUtil.CpStockCode')
        self.__codemgr = client.Dispatch('CpUtil.CpCodeMgr')
        self.__stockchart = client.Dispatch('CpSysDib.StockChart')
        self.__marketeye = client.Dispatch('CpSysDib.MarketEye')
        self.__stock_code_list = None
        self.__industry_per_memory = dict()

    def isconnect_cybos(self):
        return self.__cybos.IsConnect

    def get_stock_by_idx(self, idx):
        name = self.__stockcode.GetData(1, idx)
        code = self.__stockcode.GetData(0, idx)
        fullcode = self.__stockcode.GetData(2, idx)
        self.__marketeye.SetInputValue(0, self.MARKETEYE_TYPE)
        self.__marketeye.SetInputValue(1, code)
        self.__marketeye.BlockRequest()
        price = self.__marketeye.GetDataValue(0, 0)
        per = self.__marketeye.GetDataValue(1, 0)
        eps = self.__marketeye.GetDataValue(2, 0)
        nearest_month = self.__marketeye.GetDataValue(3, 0)
        industry_code = self.__codemgr.GetStockIndustryCode(code)
        try:
            industry_per = self.__industry_per_memory[industry_code]
        except KeyError:
            self.__industry_per_memory[industry_code] = self.get_industry_per_static(industry_code)
            industry_per = self.__industry_per_memory[industry_code]
        trading_amount_ratio = self.get_tarding_amount_ratio(code)
        stock = Stock(name, code, fullcode, idx, price, per, eps, nearest_month, industry_code, trading_amount_ratio, industry_per)
        return stock

    def get_stock_by_name(self, name):
        code = self.__stockcode.NameToCode(name)
        index = self.__stockcode.CodeToIndex(code)
        stock = self.get_stock_by_idx(index)
        return stock

    def get_stock_by_code(self, code):
        index = self.__stockcode.CodeToIndex(code)
        stock = self.get_stock_by_idx(index)
        return stock

    def get_stock_by_fullcode(self, fullcode):
        code = self.__stockcode.FullCodeToCode(fullcode)
        index = self.__stockcode.CodeToIndex(code)
        stock = self.get_stock_by_idx(index)
        return stock

    def get_stock_count(self):
        return self.__stockcode.GetCount()

    def get_stock_code_list_all(self):
        if self.__stock_code_list is None:
            self.__stock_code_list = self.__codemgr.GetStockListByMarket(1)
        return self.__stock_code_list

    def get_share_code_list_all(self):
        stock_code_list = self.get_stock_code_list_all()
        return (x for x in stock_code_list if self.get_stock_section_kind_by_code(x) == SECTION_KIND_SHARE)

    def get_etn_code_list_all(self):
        stock_code_list = self.get_stock_code_list_all()
        return (x for x in stock_code_list if self.get_stock_section_kind_by_code(x) == SECTION_KIND_ETN)

    def get_present_code_list_all(self):
        stock_code_list = self.get_stock_code_list_all()
        return (x for x in stock_code_list if self.get_stock_section_kind_by_code(x) == SECTION_KIND_PRESENT)

    def get_code_list_by_groupcode(self, code):
        return self.__codemgr.GetGroupCodeList(code)

    def get_industry_code_list(self):
        return {self.__codemgr.GetIndustryName(code): code for code in self.__codemgr.GetIndustryList()}

    def get_stock_name_by_code(self, code):
        return self.__codemgr.CodeToName(code)

    def get_stock_section_kind_by_code(self, code):
        return self.__codemgr.GetStockSectionKind(code)

    def get_stock_chart_by_period(self, code, end_day, start_day, chart_type=STOCKCHART_CHARTTYPE_DAY_CODE):
        # 가장 최근 가격이 가장 앞에 옴

        self.__stockchart.SetInputValue(0, code)
        self.__stockchart.SetInputValue(1, ord('1'))
        self.__stockchart.SetInputValue(2, end_day)
        self.__stockchart.SetInputValue(3, start_day)
        self.__stockchart.SetInputValue(5, self.CHART_DATA_TYPE)
        self.__stockchart.SetInputValue(6, chart_type)
        self.__stockchart.SetInputValue(9, ord('1'))
        self.__stockchart.BlockRequest()
        return [Chart(code, *[self.__stockchart.GetDataValue(key, i) for key in range(self.__stockchart.GetHeaderValue(1))]) for i in range(self.__stockchart.GetHeaderValue(3))]

    def get_stock_chart_by_count(self, code, data_count, chart_type=STOCKCHART_CHARTTYPE_DAY_CODE):
        # 가장 최근 가격이 가장 앞에 옴
        self.__stockchart.SetInputValue(0, code)
        self.__stockchart.SetInputValue(1, ord('2'))
        self.__stockchart.SetInputValue(4, data_count)
        self.__stockchart.SetInputValue(5, self.CHART_DATA_TYPE)
        self.__stockchart.SetInputValue(6, chart_type)
        self.__stockchart.SetInputValue(9, ord('1'))
        self.__stockchart.BlockRequest()
        return [Chart(code, *[self.__stockchart.GetDataValue(key, i) for key in range(self.__stockchart.GetHeaderValue(1))]) for i in range(self.__stockchart.GetHeaderValue(3))]

    def get_tarding_amount_ratio(self, code, period=60):
        self.__stockchart.SetInputValue(0, code)
        self.__stockchart.SetInputValue(1, ord('2'))
        self.__stockchart.SetInputValue(4, period)
        self.__stockchart.SetInputValue(5, STOCKCHART_TRADING_QUTATION_CODE)
        self.__stockchart.SetInputValue(6, STOCKCHART_CHARTTYPE_DAY_CODE)
        self.__stockchart.SetInputValue(9, ord('1'))
        self.__stockchart.BlockRequest()
        volume_list = np.asarray([self.__stockchart.GetDataValue(0, i) for i in range(self.__stockchart.GetHeaderValue(3))])
        if len(volume_list) == 0:
            return 0
        else:
            averageVolume = (np.sum(volume_list) - volume_list[0]) / (volume_list.shape[0] - 1)
            return volume_list[0] / averageVolume

    def get_industry_per_static(self, industry_group_code):
        code_list = self.get_code_list_by_groupcode(industry_group_code)
        self.__marketeye.SetInputValue(0, MARKETEYE_PER_CODE)
        self.__marketeye.SetInputValue(1, code_list)
        self.__marketeye.BlockRequest()
        per_list = np.asarray([self.__marketeye.GetDataValue(0, i) for i in range(self.__marketeye.GetHeaderValue(2))])
        mean_per = np.mean(per_list)
        max_per = np.max(per_list)
        min_per = np.min(per_list)
        return {'mean' : mean_per, 'max': max_per, 'min': min_per}


class CybosTrader(Singleton):
    def __init__(self):
        self.__tradeutil = client.Dispatch('CpTrade.CpTdUtil')
        self.__trade0311 = client.Dispatch('CpTrade.CpTd0311')
        self.__trade9061 = client.Dispatch('CpTrade.CpTdNew9061')
        self.__tradeutil.TradeInit()
        self.__account_number = self.__tradeutil.AccountNumber[0]

    def buy_stock_designation(self, code, amount, price):
        self.__trade0311.SetInputValue(0, 2)
        self.__trade0311.SetInputValue(1, self.__account_number)
        self.__trade0311.SetInputValue(3, code)
        self.__trade0311.SetInputValue(4, amount)
        self.__trade0311.SetInputValue(5, price)
        self.__trade0311.SetInputValue(7, 1)
        self.__trade0311.SetInputValue(8, TRADE_TYPE_DESIGNATION)
        self.__trade0311.BlockRequest()

    def buy_stock_best(self, code, amount):
        self.__trade0311.SetInputValue(0, 2)
        self.__trade0311.SetInputValue(1, self.__account_number)
        self.__trade0311.SetInputValue(3, code)
        self.__trade0311.SetInputValue(4, amount)
        self.__trade0311.SetInputValue(8, TRADE_TYPE_BEST)
        self.__trade0311.BlockRequest()

    def buy_stock_first(self, code, amount):
        self.__trade0311.SetInputValue(0, 2)
        self.__trade0311.SetInputValue(1, self.__account_number)
        self.__trade0311.SetInputValue(3, code)
        self.__trade0311.SetInputValue(4, amount)
        self.__trade0311.SetInputValue(8, TRADE_TYPE_FIRST)
        self.__trade0311.BlockRequest()

    def reserve_buy_stock_designation(self, code, amount, price):
        self.__trade9061.SetInputValue(0, self.__account_number)
        self.__trade9061.SetInputValue(2, '2')
        self.__trade9061.SetInputValue(3, code)
        self.__trade9061.SetInputValue(4, amount)
        self.__trade9061.SetInputValue(5, TRADE_TYPE_DESIGNATION)
        self.__trade9061.SetInputValue(6, price)
        self.__trade9061.SetInputValue(7, ord('1'))
        self.__trade9061.BlockRequest()

    def reserve_buy_stock_best(self, code, amount):
        self.__trade9061.SetInputValue(0, self.__account_number)
        self.__trade9061.SetInputValue(2, '2')
        self.__trade9061.SetInputValue(3, code)
        self.__trade9061.SetInputValue(4, amount)
        self.__trade9061.SetInputValue(5, TRADE_TYPE_BEST)
        self.__trade9061.SetInputValue(7, ord('1'))
        self.__trade9061.BlockRequest()

    def reserve_buy_stock_first(self, code, amount):
        self.__trade9061.SetInputValue(0, self.__account_number)
        self.__trade9061.SetInputValue(2, '2')
        self.__trade9061.SetInputValue(3, code)
        self.__trade9061.SetInputValue(4, amount)
        self.__trade9061.SetInputValue(5, TRADE_TYPE_FIRST)
        self.__trade9061.SetInputValue(7, ord('1'))
        self.__trade9061.BlockRequest()
