from flask import Flask, render_template, url_for, request, redirect
from random import randint

app = Flask(__name__)

tasks = [
    {
        "id": 1,
        "name": "Be the Best At Coding",
        # checkbox is checked or not
        "checked": False,
    },
    {"id": 1, "name": "Hit The Gym", "checked": True},
]


@app.route("/")
@app.route("/home", methods=["GET", "POST"])  # methods are (get) and (post)
def home():
    if request.method == "POST":
        todo_name = request.form["todo_name"]
        cur_id = randint(1, 1000)
        tasks.append({
            "id" : cur_id,
            "name" : todo_name,
            "checked" : False,
        })

    return render_template("index.html", tasks=tasks)

# <int:todo_id> = its gonna get an integer thats called todo_id \
# so the checked is for that
@app.route("/checked<int:todo_id>", methods=["POST"])
def checked_todo(todo_id):
    for task in tasks:
        if task['id'] == todo_id:
            task["checked"] = not task["checked"]
            break
    
    return redirect(url_for("home"))
    

@app.route("/delete<int:todo_id>", methods=["POST"])
def delete_todo(todo_id):
    global tasks
    for task in tasks:
        if task["id"] == todo_id:
            tasks.remove(task)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
