from flask import request
from flask_restplus import Resource, abort, reqparse, fields
from app import api
from utils.globals import *
from utils.model import *
from utils.request_handling import *
import json

todo = api.namespace('todo', description='Todo List Services')

# open json file, the root is app.py
with open("./static/propertydatabase.json", encoding="utf-8") as file:
    todo_json = json.load(file)
file.close()


# return all the information that csv has.
@todo.route("/", strict_slashes=False)
class Todo(Resource):
    @todo.response(200, 'Success', property_ori)
    @todo.expect(property_ori)
    @todo.doc(description='''
        Gets the information for the property list.
    ''')
    def get(self):
        return todo_json

    @todo.response(404, 'Invalid Id')
    @todo.response(400, 'Invalid body')
    @todo.response(200, 'Success')
    @todo.expect(property_details)
    @todo.doc(description='''
        Create a property item and store in json file.
    ''')
    def post(self):
        j = get_request_json()
        (Id, lot, ad, subp, sub, st, pc) = unpack(j, 'id', 'Lots', 'Address',
                                                  'Suburb_PostCode', 'Suburb', 'Street', 'PostCode')
        if str(Id) in todo_json.keys():
            abort(404)
        todo_json[str(Id)] = {
            'Lots': lot,
            'Address': ad,
            'Suburb_PostCode': subp,
            'Suburb': sub,
            'Street': st,
            'PostCode': pc
        }
        with open("./static/propertydatabase.json", 'w') as json_file:
            # make it more readable and pretty
            json_file.write(json.dumps(todo_json, indent=4))
            json_file.close()
        return 'Success'

    @todo.response(404, 'Invalid Id')
    @todo.response(400, 'Invalid body')
    @todo.response(200, 'Success')
    @todo.expect(property_details)
    @todo.doc(description='''
                    Update a property item in json file.
                ''')
    def put(self):
        j = get_request_json()
        (Id, lot, ad, subp, sub, st, pc) = unpack(j, 'id', 'Lots', 'Address',
                                                  'Suburb_PostCode', 'Suburb', 'Street', 'PostCode')
        if str(Id) not in todo_json.keys():
            abort(404)
        todo_json[str(Id)] = {
            'Lots': lot,
            'Address': ad,
            'Suburb_PostCode': subp,
            'Suburb': sub,
            'Street': st,
            'PostCode': pc
        }
        with open("./static/propertydatabase.json", 'w') as json_file:
            # make it more readable and pretty
            json_file.write(json.dumps(todo_json, indent=4))
            json_file.close()
        return {'message': 'Success'}

    @todo.response(404, 'Invalid Id')
    @todo.response(400, 'Invalid body')
    @todo.response(200, 'Success')
    @todo.expect()
    @todo.param('id', 'the id of the item to delete')
    @todo.doc(description='''
            Delete a property item from json file.
        ''')
    def delete(self):
        Id = get_request_arg('id', int, required=True)
        if str(Id) not in todo_json.keys():
            abort(404)
        todo_json.pop(str(Id))
        with open("./static/propertydatabase.json", 'w') as json_file:
            # make it more readable and pretty
            json_file.write(json.dumps(todo_json, indent=4))
            json_file.close()
        return {'message': 'Success'}, 200


