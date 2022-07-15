from flask import Flask, render_template, redirect, request, url_for
from __main__ import app, db, Todo

@app.route('/', methods=['POST', 'GET'])
def index(): 
    if request.method == 'POST': 
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'
    else: 
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)