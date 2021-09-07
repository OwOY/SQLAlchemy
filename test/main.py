from flask_sqlalchemy import SQLAlchemy
from flask_cors import *
from flask_restplus import Api, Namespace, fields, Resource
from flask import Flask, request, jsonify
from datetime import datetime
from UserSchema import ObjUserSchema

db = SQLAlchemy()
UserSchema = ObjUserSchema()

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
    api = Namespace('user', description='user information.')
    test = api.model('delete_user_model', {
        'type': fields.String(required=True, description="type", help="type cannot be blank."),
        'id': fields.Integer(required=True, description="id", help="id cannot be blank.")
    })
    test1 = api.model('test_model', {
        'test' : fields.Integer(required=True, description="test", help="this is test")
    })

    G_api.add_namespace(api)

    @api.route('/', methods = ['GET', 'POST'])
    class index(Resource):
        @api.route('/test')
        class test1(Resource):
            @api.expect(test)
            def post(self):
                data = request.get_json()
                output = md().search(data)
                return output

        @api.route('/test1')
        class test2(Resource):
            @api.expect(test1)
            def post(self):
                data = request.get_json()
                md().create(data)
                return data

class md(db.Model):

    __tablename__ = 'TBL_USER_INFO'

    # id
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    # 人員ID
    user_id = db.Column(db.String(50), nullable=False)
    # 姓名
    name = db.Column(db.String(50), nullable=False)
    # 部門
    department = db.Column(db.String(20), nullable=False)
    # 主管
    manager = db.Column(db.String(50), nullable=True)
    # 建立使用者ID
    create_user_id = db.Column(db.String(50), nullable=False)
    # 建立時間
    create_time = db.Column(db.DateTime, default=datetime.now())
    # 更新使用者ID
    update_user_id = db.Column(db.String(50), nullable=False)
    # 更新時間
    update_time = db.Column(db.DateTime, default=datetime.now())

    # groups = db.relationship('ObjUserGroupMapping', backref='TBL_USER_INFO')

    def __repr__(self):
        return '<TBL_USER_INFO %r>' % self.id

    def create(self, data):
        db.session.add(data)
        return db.session.commit()
    
    def search(self, data):
        # input_id = data.get('id', None)
        data = db.engine.execute('SELECT * from "TBL_USER_INFO";')
        for d in data:
            json_data = UserSchema.dump(d)

        # output = md.query.filter(md.id == input_id).all()
        # out = ObjUserInfoSchema().dump(output)
        return {'data':json_data}


if __name__ == '__main__':
    app = create_APP()
    app.run(host='0.0.0.0', port=8887, debug=True)