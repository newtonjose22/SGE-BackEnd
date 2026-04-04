from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
import uuid
from datetime import datetime


class User(Base):
    __tablename__ = 'users'  
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))

    name = Column(String, nullable=False, index=True)
    email = Column(String, nullable=False, unique=True)
    cellphone = Column(String, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False)  
    status = Column(Boolean, default=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)



class Course(Base):
    __tablename__ = 'courses'

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    course_name = Column(String, nullable=False, unique=True)
    grade = Column(Integer, nullable=False)

    subjects = relationship("Subject", back_populates="course")
    students = relationship("Student", back_populates="course")



class Student(Base):
    __tablename__ = 'students'


    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))

    user_id = Column(String, ForeignKey('users.id'))
    course_id = Column(String, ForeignKey('courses.id'))
    matricula = Column(String, default=lambda: str(uuid.uuid4()), unique=True)
    gender = Column(String, nullable=False)
    birth_date = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User")
    course = relationship("Course", back_populates="students")



class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))

    user_id = Column(String, ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.utcnow)
    user = relationship("User")
    subjects = relationship("SubjectTeach", back_populates="teacher")


class Subject(Base):
    __tablename__ = 'subjects'

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    subject_name = Column(String, nullable=False, unique=True)
    course_id = Column(String, ForeignKey('courses.id'))
    course = relationship("Course", back_populates="subjects")
    teachers = relationship("SubjectTeach", back_populates="subject")

class SchoolClasse(Base):
    __tablename__ = 'classes'

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))

    name = Column(String, nullable=False)  

    course_id = Column(String, ForeignKey('courses.id'))

    course = relationship("Course")

class Frequency(Base):
    __tablename__ = 'frequencies'
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))

    student_id = Column(String, ForeignKey('students.id'))
    subject_id = Column(String, ForeignKey('subjects.id'))
    presence = Column(Boolean, nullable=False)
    date = Column(DateTime, default=datetime.utcnow)

    student = relationship("Student")
    subject = relationship("Subject")

class SubjectTeach(Base):
    __tablename__ = 'subject_teach'
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))

    teacher_id = Column(String, ForeignKey('teachers.id'))
    subject_id = Column(String, ForeignKey('subjects.id'))

    teacher = relationship("Teacher", back_populates="subjects")
    subject = relationship("Subject", back_populates="teachers")