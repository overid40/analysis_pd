# test json

import sys
from urllib.request import Request, urlopen
from datetime import datetime
import json

try:
    url = 'http://kickscar.cafe24.com:8080/myapp-api/api/user/list'
    request = Request(url)
    resp = urlopen(request)
    resp_body = resp.read().decode("utf-8")
    print(type(resp_body), ":", resp_body)

    json_result = json.loads(resp_body)
    print(type(json_result), ":", json_result)

    data = json_result['data']
    print(type(data), ":", data)
except Exception as e:
    print('%s %s' % (e, datetime.now()), file=sys.stderr)