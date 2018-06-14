from analysis_pd.collect.api import api as pdapi

'''
# test for pd_gen_url
url = collect.api.api.pd_gen_url(
    'http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList',
    YM='{0:04d}{1:02d}'.format(2017, 1),
    SIDO='서울특별시',
    GUNGU='',
    RES_NM='',
    numOfRows=10,
    _type='json')

print(url)
'''

#for items in collect.api.api.pd_fetch_tourspot_visitor(2017, 1, '서울특별시'):
#    print(items)

# test for pd_fetch_tourspot_visitor
for items in pdapi.pd_fetch_tourspot_visitor(district1='서울특별시', year=2012, month=7):
    print(items)

#item = pdapi.pd_fetch_foreign_visitor(112, 2012, 7)
#print(item)
