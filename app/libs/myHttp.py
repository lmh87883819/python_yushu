import requests

#爬虫 scrapy, requests + beautiful soap

class Http:
    # 经典类和新式类
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        # restful
        # json
        if r.status_code != 200:
            return r.json() if return_json else r.text
        return r.json() if return_json else r.text