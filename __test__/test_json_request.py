# test for web_request.json_request

from analysis_pd.collect.api import web_request as wr

url = 'http://kickscar.cafe24.com:8080/myapp-api/api/user/list'


def success_fetch_user_list(response):
    print(response)


def error_fetch_user_list(e):
    print(e)


wr.json_request(url=url, success=success_fetch_user_list, error=error_fetch_user_list)

"""
json_result = wr.json_request(url)
print(json_result)
"""