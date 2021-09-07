from flask_cors import *
from flask_restplus import Api
from flask import Flask
from datetime import datetime
from model.database import db


def create_APP():
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:test@127.0.0.1:5432/test'
    CORS(app, supports_credentials=True)
    # app.config.from_object('cfg')
    db.init_app(app)
    initRouting(app)
    return app

def initRouting(app):
    G_api = Api(app, version='1.0', title=u'test',
                description=u'this is test demo',
                )
    createApiUi(G_api)

def createApiUi(G_api):
    from APIGUI.UserInfo import api
    G_api.add_namespace(api)


if __name__ == '__main__':
    app = create_APP()
    app.run(host='0.0.0.0', port=8887, debug=True)