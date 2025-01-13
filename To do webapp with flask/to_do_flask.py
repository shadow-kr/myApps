from flask import Flask, request, jsonify, render_template, redirect, url_for
import json
import webbrowser
from threading import Timer

app = Flask(__name__)

#http://127.0.0.1:5000
json_file_path = "./Run/Current_project/Python new project 24/To do webapp with flask/tasks.json"

def load_tasks():
    try:
        with open(json_file_path, 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks

# Save tasks to a JSON file
def save_tasks(tasks):
    with open(json_file_path, 'w') as file:
        json.dump(tasks, file)




@app.route('/')
def index():
    tasks = load_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = load_tasks()
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    tasks = load_tasks()
    new_task = request.form.to_dict()
    tasks.append(new_task)
    save_tasks(tasks)
    return render_template('index.html', tasks=tasks)

@app.route('/tasks/import', methods=['POST'])
def import_tasks():
    imported_tasks = request.json
    save_tasks(imported_tasks)
    return jsonify(imported_tasks), 201


@app.route('/tasks/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
        save_tasks(tasks)
    return redirect(url_for('index'))

# def open_browser():
#     webbrowser.open_new('http://127.0.0.1:5000')

if __name__ == '__main__':
    # Timer(1, open_browser).start()
    app.run(debug=True)
    
