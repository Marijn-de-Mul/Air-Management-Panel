from flask import Flask, render_template, redirect, request, url_for
from __main__ import app, db, Todo

@app.route('/update/<int:id>', methods=['GET', 'POST']) 
def update(id): 
    
        task = Todo.query.get_or_404(id)
    
        if request.method == 'POST': 
            task.content = request.form['content']

            try:
                db.session.commit()
                return redirect('/')
            except:
                return 'There was an issue adding your task'
        
        else: 
            return render_template('update.html', task=task)