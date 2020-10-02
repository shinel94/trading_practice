from abc import abstractmethod, ABCMeta
from VO.stock import Stock


class BaseCrawler(metaclass=ABCMeta):
    def __init__(self):
        pass

    def crawl(self, page_data):
        data = self._crawl(page_data)
        return data

    @abstractmethod
    def _crawl(self, page_data):
        raise NotImplementedError
