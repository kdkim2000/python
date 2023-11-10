from flask import Flask, request
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='Task API', description='A simple Task API')

ns = api.namespace('tasks', description='Task operations')

task = api.model('Task', {
    'id': fields.Integer(readonly=True, description='The task unique identifier'),
    'task': fields.String(required=True, description='The task details'),
})

TASKS = []

@ns.route('/')
class TaskList(Resource):
    @ns.doc('list_tasks')
    def get(self):
        """List all tasks"""
        return TASKS

    @ns.doc('create_task')
    @ns.expect(task)
    @ns.marshal_with(task, code=201)
    def post(self):
        """Create a new task"""
        new_task = api.payload
        new_task['id'] = len(TASKS) + 1
        TASKS.append(new_task)
        return new_task, 201

@ns.route('/<int:id>')
@ns.response(404, 'Task not found')
@ns.param('id', 'The task identifier')
class Task(Resource):
    @ns.doc('get_task')
    @ns.marshal_with(task)
    def get(self, id):
        """Fetch a task given its identifier"""
        for task in TASKS:
            if task['id'] == id:
                return task
        api.abort(404, "Task {} doesn't exist".format(id))

    @ns.doc('delete_task')
    @ns.response(204, 'Task deleted')
    def delete(self, id):
        """Delete a task given its identifier"""
        global TASKS
        TASKS = [task for task in TASKS if task['id'] != id]
        return '', 204

    @ns.expect(task)
    @ns.marshal_with(task)
    def put(self, id):
        """Update a task given its identifier"""
        for task in TASKS:
            if task['id'] == id:
                task.update(api.payload)
                return task
        api.abort(404, "Task {} doesn't exist".format(id))

if __name__ == "__main__":
    app.run(debug=True)
