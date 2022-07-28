import requests
import json
import pandas as pd
import logging


class ECOSReader():
    def __init__(self, api_key, warning=True, language='kr'):
        self.apikey = api_key
        self.warning = warning
        self.language = language

    def api_call(self, url, api_item, to_num):
        ret = requests.get(url)
        ret_status_code, ret_text = ret.status_code, ret.text
        if ret_status_code != 200:
            return {'status_code': ret_status_code, 'text': ret_text}

        ret_json = json.loads(ret_text)
        try:
            if to_num < ret_json[api_item]['list_total_count'] and self.warning:
                logging.warning(
                    f'''조회 가능한 아이템의 수는 {ret_json[api_item]['list_total_count']}개 입니다.
                    현재 to_num={to_num}번 까지 조회했기 떄문에 일부 데이터가 누락 될 수 있습니다.
                    to_num 파라미터를 확인해 주세요
                    워닝을 보고 싶지 않으면 ECOSReader 객체 생성 시 warning=False 옵션으로 끌 수 있습니다. ''')

            return pd.DataFrame(ret_json[api_item]['row'])
        except Exception as e:
            return ret_json


    def satatistic(self, from_num=1, to_num=1000):
        api_item = 'StatisticTableList'
        url = f'http://ecos.bok.or.kr/api/{api_item}/{self.apikey}/json/{self.language}/{from_num}/{to_num}/?'
        return self.api_call(url, api_item, to_num)

    def statistic_word(self, target_word, from_num=1, to_num=10):
        api_item = 'StatisticWord'
        url = f'http://ecos.bok.or.kr/api/{api_item}/{self.apikey}/json/{self.language}/{from_num}/{to_num}/{target_word}'
        return self.api_call(url, api_item, to_num)

    def statistic_item(self, target_code, from_num=1, to_num=100):
        api_item = 'StatisticItemList'
        url = f'http://ecos.bok.or.kr/api/{api_item}/{self.apikey}/json/{self.language}/{from_num}/{to_num}/{target_code}'
        return self.api_call(url, api_item, to_num)

    def statistic_search(self, code, period, from_date, to_date, item_code='?', from_num=1, to_num=100):
        api_item = 'StatisticSearch'
        url = f'http://ecos.bok.or.kr/api/{api_item}/{self.apikey}' \
              f'/json/{self.language}/{from_num}/{to_num}/{code}/{period}/{from_date}/{to_date}/{item_code}'
        return self.api_call(url, api_item, to_num)

    def key_statistic(self, from_num=1, to_num=100):
        api_item = 'KeyStatisticList'
        url = f'http://ecos.bok.or.kr/api/{api_item}/{self.apikey}/json/{self.language}/{from_num}/{to_num}'
        return self.api_call(url, api_item, to_num)

    def statistic_meta(self, data_name, from_num=1, to_num=100):
        api_item = 'StatisticMeta'
        url = f'http://ecos.bok.or.kr/api/{api_item}/{self.apikey}/json/{self.language}/{from_num}/{to_num}/{data_name}'
        return self.api_call(url, api_item, to_num)

if __name__ == '__main__':
    # test
    er = ECOSReader("sample")
    print(er.satatistic())
    print(er.statistic_item('102Y004'))
    print(er.key_statistic(to_num=10))
    print(er.key_statistic())
    print(er.statistic_meta('경제심리지수'))
    print(er.statistic_search('200Y001', 'A', 2015, 2021))
    print(er.statistic_search('200Y001', 'A', 2015, 2021, '701040203'))

