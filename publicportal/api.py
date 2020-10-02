from publicportal.key import API_KEY
import requests
import configparser
import xml.etree.ElementTree as ET
import datetime


class PublicAPI:
    def __init__(self):
        self.__get_code_url_by_name = 'http://api.seibro.or.kr/openapi/service/CorpSvc/getIssucoCustnoByNm'
        self.__get_info_url_by_code = 'http://api.seibro.or.kr/openapi/service/CorpSvc/getIssucoBasicInfo'
        self.__get_distribution_url_by_code = 'http://api.seibro.or.kr/openapi/service/CorpSvc/getStkDistributionShareholderStatus'

    @property
    def api_key(self):
        return API_KEY

    def get_code_by_name(self, name):
        """
        한국예탁결제원에서 제공하는 기업 코드를 회사명으로 검색합니다.
        :param name: 회사명
        :return: dict {'name', 'code'}
        """
        query_params = {'ServiceKey':self.api_key,
                        'issucoNm': name,
                        'numOfRows': str(5000)}
        request_url = self.__get_code_url_by_name + '?'
        for k, v in query_params.items():
            request_url = f'{request_url}{k}={v}&'
        res = requests.get(request_url[:-1])
        root = ET.fromstring(res.text)
        from_tags = root.iter('items')
        result = dict()
        for items in from_tags:
            for item in items.iter('item'):
                if name in item.find('issucoNm').text.split():
                    result['name'] = item.find('issucoNm').text
                    result['code'] = item.find('issucoCustno').text
        return result

    def get_info_by_code(self, code):
        """
        code를 통해서 기업 정보를 가져오는 메서드드
        :pram code:
        :return:
        apliDt : 상장일
        bizno : 사업자 번호
        ceoNm : CEO명
        engCustNm : 영문 회사명
        foundDt : 설립일
        homepAddr : 홈페이지 주소
        pval : 액면가
        totalStkcnt : 총발행 주식 수
        """
        query_params = {'ServiceKey': self.api_key,
                        'issucoCustno': code.replace('0', '')}
        request_url = self.__get_info_url_by_code + '?'
        for k, v in query_params.items():
            request_url = f'{request_url}{k}={v}&'
        res = requests.get(request_url[:-1])
        root = ET.fromstring(res.text)
        from_tags = root.iter('item')
        result = dict()
        for item in from_tags:
            result['apliDt'] = item.find('apliDt').text
            result['bizno'] = item.find('bizno').text
            result['ceoNm'] = item.find('ceoNm').text
            result['engCustNm'] = item.find('engCustNm').text
            result['foundDt'] = item.find('founDt').text
            result['pval'] = item.find('pval').text
            result['totalStkcnt'] = item.find('totalStkCnt').text
        return result

    def get_stock_dist_by_code(self, code, date=None):
        """

        :param code:
        :param date:
        :return:
        shrs: 주주 수
        shrsRatio: 주주 비율
        stkDistbutTpnm: 구분명
        stkqty: 주식 수
        stkqtyRatio: 주식 비율
        """
        if date is None:
            date = datetime.datetime.today().strftime('%Y%m%d')
        query_params = {'ServiceKey': self.api_key,
                        'issucoCustno': code.replace('0', ''),
                        'rgtStdDt': date}
        request_url = self.__get_distribution_url_by_code + '?'
        for k, v in query_params.items():
            request_url = f'{request_url}{k}={v}&'
        res = requests.get(request_url[:-1])
        print(res.text)
        root = ET.fromstring(res.text)
        from_tags = root.iter('items')
        result_list = []
        for items in from_tags:
            for item in items.iter('item'):
                result = {
                    'shrs': item.find('shrs').text,
                    'shrs_ratio': item.find('shrsRatio').text,
                    'stk_dist_name': item.find('stkDistbutTpnm').text,
                    'stk_qty': item.find('stkqty').text,
                    'stk_qty_ratio': item.find('stkqtyRatio').text
                }
                result_list.append(result)
        return result_list

if __name__ == '__main__':
    api = PublicAPI()
    data = api.get_code_by_name('삼성전자')
    print(data)
    data = api.get_info_by_code(code='593')
    print(data)
    data = api.get_stock_dist_by_code(code='593', date='20200931')
    print(data)
