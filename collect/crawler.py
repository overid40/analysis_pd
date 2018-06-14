import os
import json
from .api import api

RESULT_DIRECTORY = '__results__/crawling'


def preprocess_foreign_visitor(data):
    # ed
    del data['ed']

    # deCd
    del data['edCd']

    # rnum
    del data['rnum']

    #나라 코드
    data['country_code'] = data['natCd']
    del data['natCd']

    # 나라 이름
    data['country_name'] = data['natKorNm'].replace(' ', '')
    del data['natKorNm']

    # 방문자 수
    data['visit_count'] = data['num']
    del data['num']

    # 년월
    if 'ym' not in data:
        data['date'] = ''
    data['data'] = data['ym']
    del data['ym']


def preprocess_tourspot_visitor(data):
    # addrCd
    del data['addrCd']

    # count_foreigner
    data['count_foreigner'] = data['csForCnt']
    del data['csForCnt']

    # count_locals
    data['count_locals'] = data['csNatCnt']
    del data['csNatCnt']

    # restrict2
    data['restrict2'] = data['gungu']
    del data['gungu']

    # tourist_spot
    data['tourist_spot'] = data['resNm']
    del data['resNm']

    # rnum
    del data['rnum']

    # restrict1
    data['restrict1'] = data['sido']
    del data['sido']

    # date
    if 'ym' not in data:
        data['date'] = ''
    data['data'] = data['ym']
    del data['ym']


def crawling_foreign_visitor(country, start_year, end_year):
    results = []
    for year in range(start_year, end_year+1):
        for month in range(1, 13):
        #for month in range(1, 4):
            # print("fetch..." + country[0] + ":" + str(year) + "-" + str(month))
            data = api.pd_fetch_foreign_visitor(country[1], year, month)
            if data is None:
                continue

            preprocess_foreign_visitor(data)
            results.append(data)

    # save data to file
    # print(results)
    filename = '%s/%s(%s)_foreignvisitor_%s_%s.json' % (RESULT_DIRECTORY, country[0], country[1], start_year, end_year)
    with open(filename, 'w', encoding='utf-8') as outfile:
        json_string = json.dumps(results, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(json_string)


if not os.path.exists(RESULT_DIRECTORY):
    os.makedirs(RESULT_DIRECTORY)


def crawling_tourspot_visitor(district, start_year, end_year):
    results = []
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
        # for month in range(1, 4):
            # print("fetch..." + country[0] + ":" + str(year) + "-" + str(month))
            datass = api.pd_fetch_tourspot_visitor(district, year=year, month=month)
            for datas in datass:
                for data in datas:
                    preprocess_tourspot_visitor(data)
                results.append(datas)
    print(results)

    # save data to file
    # print(results)
    filename = '%s/%s_touristspot_%s_%s.json' % (RESULT_DIRECTORY, district, start_year, end_year)
    with open(filename, 'w', encoding='utf-8') as outfile:
        json_string = json.dumps(results, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(json_string)


if not os.path.exists(RESULT_DIRECTORY):
    os.makedirs(RESULT_DIRECTORY)

