from constant.constant import STOCKCHART_CHARTTYPE_DAY_CODE
from cybos.cybos import Cybos
from tqdm import tqdm

cybos = Cybos()

# print(cybos.isconnect_cybos())
# print(cybos.get_stock_count())
# print(cybos.get_stock_by_idx(0))
# print(cybos.get_stock_by_name('동화약품'))
# print(cybos.get_stock_by_code('A000020'))
# print(cybos.get_stock_by_fullcode('KR7000020008'))
#
# for i in range(10):
#     print(cybos.get_stock_by_idx(i).name)
#
# print(cybos.get_stock_by_name(NAVER_NAME))

# print(cybos.get_stock_code_list_all())
# kospi = dict()
# with open('C:/Users/HY/Desktop/TradingPractice/trading_practice/result_file/kospi.csv', 'w', encoding='utf-8') as f:
#     f.write(f'name, code, section\n')
#     for code in cybos.get_stock_code_list_all():
#         name = cybos.get_stock_name_by_code(code)
#         section = cybos.get_stock_section_kind_by_code(code)
#         # print(type(section))
#         f.write(f'{name}, {code}, {section}\n')
#     f.close()
#
# with open('C:/Users/HY/Desktop/TradingPractice/trading_practice/result_file/share.csv', 'w', encoding='utf-8') as f:
#     f.write(f'name, code, section\n')
#     for code in cybos.get_share_code_list_all():
#         name = cybos.get_stock_name_by_code(code)
#         section = cybos.get_stock_section_kind_by_code(code)
#         # print(type(section))
#         f.write(f'{name}, {code}, {section}\n')
#     f.close()
#
# with open('C:/Users/HY/Desktop/TradingPractice/trading_practice/result_file/etn.csv', 'w', encoding='utf-8') as f:
#     f.write(f'name, code, section\n')
#     for code in cybos.get_etn_code_list_all():
#         name = cybos.get_stock_name_by_code(code)
#         section = cybos.get_stock_section_kind_by_code(code)
#         # print(type(section))
#         f.write(f'{name}, {code}, {section}\n')
#     f.close()
#
#
#
# from constant.constant import STOCKCHART_CHARTTYPE_DAY_CODE
# print(cybos.get_stock_chart_by_period('A003540', '20200915', '20200901', STOCKCHART_CHARTTYPE_DAY_CODE))
# print(cybos.get_stock_chart_by_period('A003540', 20200915, 20200901, STOCKCHART_CHARTTYPE_DAY_CODE))
# print(cybos.get_stock_chart_by_count('A003540', 100, STOCKCHART_CHARTTYPE_DAY_CODE))
from time import sleep
count = 0
with open('C:/Users/HY/Desktop/TradingPractice/trading_practice/result_file/kospi.csv', 'w', encoding='utf-8') as f:
    f.write(f'index, name, code, price, PER, EPS, 최근분기년월, 최근거래량증가비율, 산업평균per, 산업per최대, 산업per최소\n')
    for code in cybos.get_share_code_list_all():
        stock = cybos.get_stock_by_code(code)
        f.write(f'{stock.index}, {stock.name}, {stock.code}, {stock.price}, {stock.per}, {stock.eps}, {stock.nearest_month}, {stock.trading_amount_ratio}, {stock.industry_mean_per}, {stock.industry_max_per}, {stock.industry_min_per}\n')
        sleep(0.1)
        count += 1
        if count > 100:
            break
    f.close()

# print(cybos.get_industry_code_list())
# from constant.constant import INDUSTRY_CODE_CHEM
# print(cybos.get_code_list_by_groupcode(INDUSTRY_CODE_CHEM))
