from flask import Flask, render_template, redirect, request, url_for
from __main__ import app, db, Todo

from __main__ import app

@app.route('/delete/<int:id>') 
def delete(id): 
    task_to_delete = Todo.query.get_or_404(id)
    
    try: 
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except: 
        return 'There was an issue deleting your task'