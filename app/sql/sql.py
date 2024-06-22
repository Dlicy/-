import sqlalchemy
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///sql.db', echo = True)
Base = declarative_base()
meta_data = sqlalchemy.MetaData()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    ac_rate = Column(Float)
    selected_courses = relationship('Course', secondary='student_course_association', back_populates='students')
    submissions = relationship('Submission', back_populates='student')

class Submission(Base):
    __tablename__ = 'submissions'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    student = relationship('Student', back_populates='submissions')
    submit_time = Column(String)
    language = Column(String)
    result = Column(String)
    score = Column(Integer)
    code_length = Column(Integer)
    memory = Column(Integer)
    runtime = Column(Integer)
    problem_id = Column(Integer, ForeignKey('problems.id'))
    problem = relationship('Problem', backref='submissions')

class Problem(Base):
    __tablename__ = 'problems'

    id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'))
    course = relationship('Course', backref='problems')
    upload_user = Column(String)
    problem_type = Column(String)
    details = Column(String)
    ac_rate = Column(Float)
    test_cases = relationship('TestCase', back_populates='problem')

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    semester = Column(String)
    teacher = Column(String)
    students = relationship('Student', secondary='student_course_association', back_populates='selected_courses')
    exams = relationship('Exam', back_populates='course')

class Exam(Base):
    __tablename__ = 'exams'

    id = Column(Integer, primary_key=True)
    exam_type = Column(String)
    format = Column(String)
    location = Column(String)
    time = Column(String)
    password = Column(String)
    teacher = Column(String)
    course_id = Column(Integer, ForeignKey('courses.id'))
    course = relationship('Course', back_populates='exams')

class TestCase(Base):
    __tablename__ = 'test_cases'

    id = Column(Integer, primary_key=True)
    input_data = Column(String)
    output_data = Column(String)
    problem_id = Column(Integer, ForeignKey('problems.id'))
    problem = relationship('Problem', back_populates='test_cases')

class Daily(Base):
    __tablename__ = 'daily'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    student_id = Column(Integer, ForeignKey('students.id'))
    problem_id = Column(Integer, ForeignKey('problems.id'))

class Weekly(Base):
    __tablename__ = 'weekly'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    daily_id = Column(Integer, ForeignKey('daily.id'))

class Monly(Base):
    __tablename__ = 'monly'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    weekly_id = Column(Integer, ForeignKey('weekly.id'))

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)


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

class Problem(Base):
    __tablename__ = 'problems'

    id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'))
    course = relationship('Course', backref='problems')
    upload_user = Column(String)
    problem_type = Column(String)
    details = Column(String)
    ac_rate = Column(Float)
    test_cases = relationship('TestCase', back_populates='problem')

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    semester = Column(String)
    teacher = Column(String)
    students = relationship('Student', secondary='student_course_association', back_populates='selected_courses')
    exams = relationship('Exam', back_populates='course')

class Exam(Base):
    __tablename__ = 'exams'

    id = Column(Integer, primary_key=True)
    exam_type = Column(String)
    format = Column(String)
    location = Column(String)
    time = Column(String)
    password = Column(String)
    teacher = Column(String)
    course_id = Column(Integer, ForeignKey('courses.id'))
    course = relationship('Course', back_populates='exams')

class TestCase(Base):
    __tablename__ = 'test_cases'

    id = Column(Integer, primary_key=True)
    input_data = Column(String)
    output_data = Column(String)
    problem_id = Column(Integer, ForeignKey('problems.id'))
    problem = relationship('Problem', back_populates='test_cases')

class Daily(Base):
    __tablename__ = 'daily'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    student_id = Column(Integer, ForeignKey('students.id'))
    problem_id = Column(Integer, ForeignKey('problems.id'))

class Weekly(Base):
    __tablename__ = 'weekly'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    daily_id = Column(Integer, ForeignKey('daily.id'))

class Monly(Base):
    __tablename__ = 'monly'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    weekly_id = Column(Integer, ForeignKey('weekly.id'))
# 其他模型类的定义

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)