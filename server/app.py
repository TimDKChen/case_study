from flask import Flask
from flask_restplus import Api
from flask_cors import CORS

app = Flask(__name__)
app.config['FLASK_APP'] = 'app.py'
CORS(app)
api = Api(app)

import namespaces.todo

if __name__ == '__main__':
    app.run(debug=True)
