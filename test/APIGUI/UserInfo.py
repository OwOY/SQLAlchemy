from flask_restplus import Namespace, Resource
from flask import request
from model.UserInfo import md

api = Namespace('user', description='user information.')
test = api.model('delete_user_model', {
    'type': fields.String(required=True, description="type", help="type cannot be blank."),
    'id': fields.Integer(required=True, description="id", help="id cannot be blank.")
})
test1 = api.model('test_model', {
    'test' : fields.Integer(required=True, description="test", help="this is test")
})

@api.route('/test')
class Test(Resourse):
    @api.expect(test)
    def post(self):
        data = request.get_json()
        return srv.test(data)

@api.route('/test1')
class Test1(Resourse):
    @api.expect(test1)
    def post(self):
        data = request.get_json()
        return srv.test(data)
