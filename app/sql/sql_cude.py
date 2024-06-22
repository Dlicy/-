import sqlalchemy
from sqlalchemy.orm import sessionmaker
from app.sql.models import Student

engine = sqlalchemy.create_engine('sqlite:///sql.db', echo=True)
Session = sessionmaker(bind=engine)

# 创建(INSERT)
def create_student(username, email, password, ac_rate):
    session = Session()
    new_student = Student(username=username, email=email, password=password, ac_rate=ac_rate)
    session.add(new_student)
    session.commit()
    return new_student

# 读取(SELECT)
def get_all_students():
    session = Session()
    return session.query(Student).all()

def get_student_by_id(student_id):
    session = Session()
    return session.query(Student).filter_by(id=student_id).first()

# 更新(UPDATE)
def update_student_email(student_id, new_email):
    session = Session()
    student = session.query(Student).filter_by(id=student_id).first()
    student.email = new_email
    session.commit()
    return student

# 删除(DELETE)
def delete_student(student_id):
    session = Session()
    student = session.query(Student).filter_by(id=student_id).first()
    session.delete(student)
    session.commit()