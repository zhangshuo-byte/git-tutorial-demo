from flask import Flask, request, jsonify

app = Flask(__name__)

# 内存存储
tasks = []
task_id_counter = 0


@app.route('/')
def index():
    return {'message': 'Welcome to Task API', 'version': '0.1.0'}


@app.route('/api/tasks', methods=['GET'])
def list_tasks():
    return jsonify([task.to_dict() for task in tasks])


@app.route('/api/tasks', methods=['POST'])
def create_task():
    global task_id_counter
    data = request.get_json()
    from src.models import Task
    task = Task(data.get('title'), data.get('description', ''))
    task_id_counter += 1
    task.id = task_id_counter
    tasks.append(task)
    response = jsonify(task.to_dict())
    response.status_code = 201
    response.headers['Location'] = f'/api/tasks/{task.id}'
    return response


@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    for task in tasks:
        if task.id == task_id:
            return jsonify(task.to_dict())
    return jsonify({'error': 'Task not found'}), 404


@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    for task in tasks:
        if task.id == task_id:
            data = request.get_json()
            if 'title' in data:
                task.title = data['title']
            if 'description' in data:
                task.description = data['description']
            if 'completed' in data:
                task.completed = data['completed']
            return jsonify(task.to_dict())
    return jsonify({'error': 'Task not found'}), 404


@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    for i, task in enumerate(tasks):
        if task.id == task_id:
            tasks.pop(i)
            return '', 204
    return jsonify({'error': 'Task not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
