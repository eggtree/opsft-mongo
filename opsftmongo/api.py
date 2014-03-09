from flask import Flask
from flask.ext.restful import Api

from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

import mng

app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return '<!DOCTYPE html><html><body>Example:<ul><li>{}</li></ul></body></html>'.format(mng.index())


if __name__ == '__main__':
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(5002)
    IOLoop.instance().start()

