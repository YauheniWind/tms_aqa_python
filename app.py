import flask
from flask_restful import Resource, Api

app = flask.Flask(__name__)
api = Api(app)


class Hello(Resource):
    def get(self):
        return 'Hello World!'


api.add_resource(Hello, '/')

if __name__ == '__main__':
    app.run('0.0.0.0', 3333)
