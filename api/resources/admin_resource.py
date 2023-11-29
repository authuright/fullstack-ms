from flask_restful import Resource
from flask import make_response, request
class AdminResource(Resource):
    def get(self):
        return make_response({"admin":{"name": "Test Admin"}},200)
    
    def post(self):

        user = request.get_json()
        user.update({ 'id':1 })
        return make_response(user, 201)
    
    def put(self):
        user = request.get_json()
        user.update({ 'id':1 })
        return make_response({"id":1, "first_name": "update Name"},200)
    
    def patch(self):
        return make_response({"id":1, "first_name": "update Name"},200)
    
    def delete(self):
        return make_response("",200)