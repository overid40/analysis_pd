# FB API Wrapper Functions
from datetime import datetime
from urllib.parse import urlencode
from .web_request import json_request
import math

SERVICE_KEY = 'aOfeFUvQLW9r7sj4YJ9ImX59DF7eObseBnnTb3LLm%2FZCiqKoGqTGr75%2Frac1mstKdLdALUq7Siel4BL1rk%2FO1Q%3D%3D'


def pd_gen_url(endpoint, **param):
    url = '%s?%s&serviceKey=%s' % (endpoint, urlencode(param), SERVICE_KEY)
    return url
    print(url)

'''
def fb_name_to_id(pagename):
    url = fb_gen_url(node=pagename, access_token=ACCESS_TOKEN)
    json_result = json_request(url=url)
    return json_result.get("id")
'''


def pd_fetch_foreign_visitor(country_code, year, month):
    endpoint = 'http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList'
    url = pd_gen_url(endpoint, YM='{0:04d}{1:02d}'.format(year, month), NAT_CD=country_code, ED_CD='E', _type='json')
    print(url)

    json_result = json_request(url=url)

    json_response = json_result.get('response')
    json_header = json_response.get('header')
    result_message = json_header.get('resultMsg')
    if 'OK' != result_message:
        print('%s Error[%s] for request %s' % (datetime.now(), result_message, url))
        return None

    json_body = json_response.get('body')
    json_items = json_body.get('items')

    return json_items.get('item') if isinstance(json_items, dict) else None


def pd_fetch_tourspot_visitor(district1='', district2='', tourspot='', year=0, month=0):
    endpoint = 'http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList'
    pageno=1
    hasnext = True
    while hasnext:
        url = pd_gen_url(endpoint, YM='{0:04d}{1:02d}'.format(year, month),
        SIDO=district1,
        GUNGU=district2,
        RES_NM=tourspot,
        numOfRows=10,
        _type='json',
        pageNo=pageno)
        # print(url)

        json_result = json_request(url=url)

        json_response = json_result.get('response')
        json_header = json_response.get('header')
        result_message = json_header.get('resultMsg')
        json_body = json_response.get('body')
        json_items = json_body.get('items')
        numofrows = json_body.get('numOfRows')
        totalcount = json_body.get('totalCount')

        if 'OK' != result_message:
            print('%s Error[%s] for request %s' % (datetime.now(), result_message, url))
            return None

        if totalcount == 0:
            break
        last_page = math.ceil(totalcount/numofrows)
        if pageno == last_page:
            hasnext=False
        else:
            pageno += 1

        yield json_items.get('item') if isinstance(json_items, dict) else None