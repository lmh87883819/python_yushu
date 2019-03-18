from app import create_app

__author__ = 'lmh'

app = create_app()
if __name__ == '__main__':
    #生产环境 Ngnix + uwisgi
    app.run(debug=app.config['DEBUG'],host='0.0.0.0',port=3000, threaded= True)