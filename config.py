import os
# configuration
CONFIG = {
    'district': '서울특별시',
    'countries': [('중국', 112), ('일본', 130), ('미국', 275)],
    'common': {
        'start_year': 2017,
        'end_year': 2017,
        'fetch': False,
        'result_directory': '__results__/crawling',
        'service_key' : 'aOfeFUvQLW9r7sj4YJ9ImX59DF7eObseBnnTb3LLm%2FZCiqKoGqTGr75%2Frac1mstKdLdALUq7Siel4BL1rk%2FO1Q%3D%3D'
    }
}

if not os.path.exists(CONFIG['common']['result_directory']):
    os.makedirs(CONFIG['common']['result_directory'])
