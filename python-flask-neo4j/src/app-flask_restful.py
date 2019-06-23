from flask import Flask, request, jsonify
from flask_restful import Resource, Api, abort
from py2neo import Graph

app = Flask(__name__)

api = Api(app, catch_all_404s=True)

g = Graph("bolt://neo4j:7687", auth=('neo4j', 'pass'))

class TodoSimple(Resource):
    def get(self, todo_id):
        res = g.run("MATCH (a:Todo) WHERE a.id = {todo_id} RETURN id(a), labels(a), a", todo_id=todo_id).data()
        return res

    def put(self, todo_id):
        data = request.form
        res = g.run("CREATE (a:Todo {data}) SET a.id = {todo_id} RETURN a", data=data, todo_id=todo_id).data()
        return res

api.add_resource(TodoSimple, '/todo/<int:todo_id>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)