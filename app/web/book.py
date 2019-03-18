from flask import jsonify, request
from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from . import web 

@web.route('/book/search/')
def search():
    '''
        q: 普通关键字/isbn
        page
    '''
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.searchByIsbn(q)
        else:
            result = YuShuBook.searchByKeyword(q, page)
        # print(result)
        return jsonify(result)
    else:
        return jsonify(form.errors)
    # return json.dumps(result), 200, {'content-type':'application/json'}