# FB API Wrapper Functions
from urllib.parse import urlencode
from .web_request import json_request

ACCESS_TOKEN = 'aOfeFUvQLW9r7sj4YJ9ImX59DF7eObseBnnTb3LLm%2FZCiqKoGqTGr75%2Frac1mstKdLdALUq7Siel4BL1rk%2FO1Q%3D%3D'
BASE_URL_FB_API = "http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList"


def pd_gen_url(endpiont=BASE_URL_FB_API, **params):
    url = '%s?%s&' % (endpiont, urlencode(params))
    return url


'''
def fb_name_to_id(pagename):
    url = fb_gen_url(node=pagename, access_token=ACCESS_TOKEN)
    json_result = json_request(url=url)
    return json_result.get("id")
'''


def pd_fetch_tourspot_visitor(pagename, since, until):
    url = pd_gen_url(node=fb_name_to_id(pagename) + "/posts",
                     fields='id,message,link,name,type,shares,reactions,created_time,comments.limit(0).summary(true).limit(0).summary(true)',
                     since=since, until=until, limit=50,
                     access_token=ACCESS_TOKEN)

    # results = []
    isnext = True
    while isnext is True:
        json_result = json_request(url=url)
        '''
        paging = None

        if json_result is None:
            paging = None
        else:
            paging = json_result.get('paging')
        '''

        paging = None if json_result is None else json_result.get('paging')  # 위의 코드 간결하게 표현
        posts = None if json_result is None else json_result.get('data')

        # results += posts  # results = results + posts

        url = None if paging is None else paging.get("next")
        isnext = url is not None  # 아래 코드 간결하게 표현

        '''
        if url is not None:
            isnext = True
        else:
            isnext = False
        '''

        # return results
        yield posts