from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sql.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    ac_rate = db.Column(db.Float)
    selected_courses = db.relationship('Course', secondary='student_course_association', back_populates='students')
    submissions = db.relationship('Submission', back_populates='student')

class Submission(db.Model):
    __tablename__ = 'submissions'

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    student = db.relationship('Student', back_populates='submissions')
    submit_time = db.Column(db.String)
    language = db.Column(db.String)
    result = db.Column(db.String)
    score = db.Column(db.Integer)
    code_length = db.Column(db.Integer)
    memory = db.Column(db.Integer)
    runtime = db.Column(db.Integer)
    problem_id = db.Column(db.Integer, db.ForeignKey('problems.id'))
    problem = db.relationship('Problem', backref='submissions')

class Problem(db.Model):
    __tablename__ = 'problems'

    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    course = db.relationship('Course', backref='problems')
    upload_user = db.Column(db.String)
    problem_type = db.Column(db.String)
    details = db.Column(db.String)
    ac_rate = db.Column(db.Float)
    test_cases = db.relationship('TestCase', back_populates='problem')

class Course(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    semester = db.Column(db.String)
    teacher = db.Column(db.String)
    students = db.relationship('Student', secondary='student_course_association', back_populates='selected_courses')
    exams = db.relationship('Exam', back_populates='course')

class Exam(db.Model):
    __tablename__ = 'exams'

    id = db.Column(db.Integer, primary_key=True)
    exam_type = db.Column(db.String)
    format = db.Column(db.String)
    location = db.Column(db.String)
    time = db.Column(db.String)
    password = db.Column(db.String)
    teacher = db.Column(db.String)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    course = db.relationship('Course', back_populates='exams')

class TestCase(db.Model):
    __tablename__ = 'test_cases'

    id = db.Column(db.Integer, primary_key=True)
    input_data = db.Column(db.String)
    output_data = db.Column(db.String)
    problem_id = db.Column(db.Integer, db.ForeignKey('problems.id'))
    problem = db.relationship('Problem', back_populates='test_cases')

class Daily(db.Model):
    __tablename__ = 'daily'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    problem_id = db.Column(db.Integer, db.ForeignKey('problems.id'))

class Weekly(db.Model):
    __tablename__ = 'weekly'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    daily_id = db.Column(db.Integer, db.ForeignKey('daily.id'))

class Monly(db.Model):
    __tablename__ = 'monly'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    weekly_id = db.Column(db.Integer, db.ForeignKey('weekly.id'))
# 其他模型类的定义

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)