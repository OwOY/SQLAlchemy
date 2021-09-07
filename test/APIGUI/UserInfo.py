from flask_restplus import Api, Namespace, fields, Resource
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