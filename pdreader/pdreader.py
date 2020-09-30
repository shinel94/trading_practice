from util.singleton import Singleton
from pandas_datareader import data as web


class PDReader(Singleton):

    def __init__(self):
        self.data_reader = web.DataReader

    def search_by_code(self, code, start_date=None, end_date=None):
        return self.data_reader(name=code, data_source='yahoo', start=start_date, end=end_date)