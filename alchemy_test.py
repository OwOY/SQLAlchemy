from flask_sqlalchemy import SQLAlchemy
from flask_restplus import Api, Namespace, fields, Resource
from flask import Flask, request
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:test@127.0.0.1:5432/test'
db = SQLAlchemy()
db.init_app(app)

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

    groups = db.relationship('ObjUserGroupMapping', backref='TBL_USER_INFO')

    def __repr__(self):
        return '<TBL_USER_INFO %r>' % self.id

api = Namespace('user', description='user information.')
test = api.model('delete_user_model', {
    'type': fields.String(required=True, description="type", help="type cannot be blank."),
    'id': fields.Integer(required=True, description="id", help="id cannot be blank.")
})
G_api = Api(app, version='1.0', title=u'test',
            description=u'this is test demo',
            )
G_api.add_namespace(api)

@api.route('/', methods = ['GET'])
class index(Resource):
    @api.route('/test')
    class test1(Resource):
        @api.expect(test)
        def get(self):
            data = request.get_json()
            return data


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=8887, debug=True)
