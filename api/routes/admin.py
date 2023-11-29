from flask import Flask,Blueprint
from flask_restful import Api

from resources import AdminResource


admin_route = Blueprint("admin_route",__name__)
api = Api(admin_route)

api.add_resource(AdminResource,'/admin')