from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app, version='1.0', title='Sample API', description='A sample API')

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        """A greeting to the world"""
        return {'message' : 'Hello, World!!!!!!'}

if __name__ == "__main__":
    app.run(debug=True)
