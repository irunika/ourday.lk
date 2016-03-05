from flask_restful import Resource
from flask import redirect, render_template, make_response
from packages.db.Mongo_Collection_Handler import Mongo_Collection_Handler

class add_user(Resource):
    def get(self):
        mongo_districts = Mongo_Collection_Handler('districts')
        districts = []
        for district in mongo_districts._get_data_({}):
            districts.append(district['_id'])
        return make_response(
            render_template('register_user.html', districts=districts)
        )