from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db=SQLAlchemy(app)

class Todo(db.Model):
    sno= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(30), nullable=False)
    title= db.Column(db.String(200), nullable=False)
    desc= db.Column(db.String(500), nullable=False)
    date_created= db.Column(db.DateTime, default=datetime.now)

    def __repr__(self) -> str:
        print(self.date_created)
        return f"{self.sno} - {self.title}"

@app.before_first_request
def create_tables():
   db.create_all()

@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method=='POST':
        name= request.form['name']
        title= request.form['title']
        desc= request.form['desc']
        todo= Todo(name=name, title= title, desc=desc)
        db.session.add(todo)
        db.session.commit()
    alltodo= Todo.query.all()
    # print(alltodo)
    return render_template('index.html', alltodo=alltodo)

@app.route('/update/<int:sno>', methods=['POST', 'GET'])
def update(sno):
    if request.method=='POST':
        name= request.form['name']
        title= request.form['title']
        desc= request.form['desc']
        todo= Todo.query.filter_by(sno=sno).first()
        todo.name= name
        todo.title= title
        todo.desc= desc
        db.session.add(todo)
        db.session.commit()
        return redirect('/')
    todo= Todo.query.filter_by(sno=sno).first()
    return render_template('update.html', todo=todo)

@app.route('/delete/<int:sno>')
def delete(sno):
    todo= Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')

@app.route('/search-result', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        search_term= request.form['search_term']
        todo= Todo.query.filter(Todo.title.contains(search_term)).all()
        return render_template('search result.html', todo=todo)


if __name__=='__main__':
    app.run(debug=True)
