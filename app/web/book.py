from flask import jsonify, request, render_template
import json
from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookCollection
from . import web 

@web.route('/book/search')
def search():
    '''
        q: 普通关键字/isbn
        page
        9787070511209
    '''
    form = SearchForm(request.args)
    books = BookCollection() 
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()
        if isbn_or_key == 'isbn':
            yushu_book.searchByIsbn(q)
        else:
            yushu_book.searchByKeyword(q, page)
        books.fill(yushu_book, q)
        # print(result)
        return json.dumps(books, default=lambda o: o.__dict__, ensure_ascii=False)
    else:
        return jsonify(form.errors)
    # return json.dumps(result), 200, {'content-type':'application/json'}

@web.route('/test')
def test():
    test = {
        'English': 'Hello World',
        'Chinese': '你好 世界'
    }
    return render_template('test.html', data = test)