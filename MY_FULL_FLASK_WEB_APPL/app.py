from flask import Flask, render_template, request, redirect
import sqlite3
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db=SQLAlchemy(app)

class Students(db.Model):
    __tablename__ = "students"
    id=db.Column(db.Integer, primary_key=True)
    student_name=db.Column(db.String(50))
    gender=db.Column(db.String(10))

    def __init__(self, student_name, gender):
        self.student_name=student_name
        self.gender=gender

    def __repr__ (self):
        return f"{self.student_name}, {self.gender}"    
    
# creating a decorator that creates all the tables in the sqlalchemy model before any request is done
@app.before_request
def create_table():
    db.create_all()

@app.route('/')
def list_students():
    students = Students.query.all()
    return render_template('index.html', students = students)

    
@app.route('/add' ,methods=['GET', 'POST'])
def add_student():
    if request.method =='GET':
        return render_template('add.html')
    
    if request.method == 'POST':
        student_name = request.form['student_name']
        gender = request.form['gender']
        student = Students(student_name=student_name, gender=gender)
        db.session.add(student)
        db.session.commit()
        return redirect('/')

@app.route('/edit<int:id>' , methods=['GET' , 'POST'])    
def edit_student(id):

    student = Students.query.get(id)
    if request.method == 'GET':
        return render_template('edit.html', student=student)
    
    if request.method == 'POST':

        student.student_name = request.form['student_name']
        student.gender = request.form['gender']
        db.session.commit()
        return redirect('/')
    

@app.route('/delete<int:id>')
def delete_student(id):
    student = Students.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return redirect('/')   

        




if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)

