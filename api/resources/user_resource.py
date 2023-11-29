from flask_restful import Resource
from flask import make_response, request

from app.app import db
from models import UserModel
from schemas import UserSchema
class UserResource(Resource):
    def get(self):
        users = db.session.query(UserModel).all()
        user_schema = UserSchema()
        user_json = user_schema.dump(users, many=True)
        return make_response({'user': user_json},200)
    
    def post(self):
        user = request.get_json()
        user_schema = UserSchema()
        new_user = UserModel(user)
        db.session.add(new_user)
        db.session.commit()
        return make_response({'user': user},201)
    
    def put(self): 
        user = request.get_json()
        user.update({ 'id':1 })
        return make_response({"id":1, "first_name": "update Name"},200)
    
    def patch(self):
        return make_response({"id":1, "first_name": "update Name"},200)
    
    def delete(self):
        return make_response("",200)