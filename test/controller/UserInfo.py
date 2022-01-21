from flask_restplus import fields, Namespace, Resource
from flask import request
from model.UserInfo import ObjUserInfo
from service.userInfo import SrvUserInfo


api = Namespace('user', description='user information.')
test = api.model('delete_user_model', {
    'type': fields.String(required=True, description="type", help="type cannot be blank."),
    'id': fields.Integer(required=True, description="id", help="id cannot be blank.")
})
test1 = api.model('test_model', {
    'test' : fields.Integer(required=True, description="test", help="this is test")
})
srv = SrvUserInfo()


@api.route('/test')
class Test(Resource):
    @api.expect(test)
    def post(self):
        data = request.get_json()
        return srv.test(data)

@api.route('/test1')
class Test1(Resource):
    @api.expect(test1)
    def post(self):
        data = request.get_json()
        return srv.test(data)
