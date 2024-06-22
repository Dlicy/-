from app.sql.models import Base, engine
from .crud import create_student, get_all_students, get_student_by_id, update_student_email, delete_student

# 创建数据库表
Base.metadata.create_all(engine)

# 使用CRUD操作
new_student = create_student('JohnDoe', 'johndoe@example.com', 'mypassword', 0.85)
print(f"Created new student: {new_student.username}")

all_students = get_all_students()
for student in all_students:
    print(f"Student: {student.username}, Email: {student.email}, AC Rate: {student.ac_rate}")

student = get_student_by_id(1)
print(f"Student found: {student.username}, Email: {student.email}, AC Rate: {student.ac_rate}")

updated_student = update_student_email(1, 'newemail@example.com')
print(f"Updated student email: {updated_student.username}, Email: {updated_student.email}")

delete_student(1)
print("Student deleted.")