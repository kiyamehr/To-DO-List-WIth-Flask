from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for


app = Flask(__name__)

tasks = ["Buy groceries", "Being The Best at Coding", "Doing college HomeWork"]


@app.route("/")
# redering the whole web
def index():
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
# adding a task
def add_task():
    new_task = request.form.get("newTask")
    if new_task:
        tasks.append(new_task)
    return redirect(url_for("index"))


# adding a completed task
@app.route("/complete", methods=["POST"])
def complete_tasks():
    completed_tasks = request.form.getlist('taskCheckbox')
    for index in map(int, completed_tasks):
        if 1 <= index <= len(tasks):
            tasks[index - 1] += " - Completed"
    return redirect(url_for('index'))

@app.route("/delete", methods=["POST"])
def delete_task():
    tasks_to_delete = request.form.getlist("taskCheckbox")
    tasks_to_delete.sort(reverse=True)
    for index in map(int, complete_tasks):
        if 1 <= index <= len(complete_tasks):
            del tasks[index - 1]
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
