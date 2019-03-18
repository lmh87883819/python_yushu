from app.libs.myHttp import Http
from flask import current_app

class YuShuBook:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={} '

    @classmethod
    def searchByIsbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        response =  Http.get(url)
        return response

    @classmethod
    def searchByKeyword(cls, keyword, page=1):
        url = cls.keyword_url.format(keyword, current_app.config['PER_PAGE'], cls.calculate_start(page))
        response =  Http.get(url)
        return response

    @staticmethod
    def calculate_start(page):
        return (page - 1) * current_app.config['PER_PAGE']