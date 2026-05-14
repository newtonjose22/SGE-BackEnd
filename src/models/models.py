from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from src.database.database import Base
import uuid
from datetime import datetime



# USERS (FUNCIONÁRIOS)

class User(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))

    name = Column(String, nullable=False, index=True)
    email = Column(String, nullable=False, unique=True)
    cellphone = Column(String, nullable=False)
    password = Column(String, nullable=False)

    # admin, diretor, secretaria, professor
    role = Column(String, nullable=False)

    status = Column(Boolean, default=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    teacher = relationship("Teacher", back_populates="user", uselist=False)


# =========================
# CURSOS
# =========================
class Course(Base):
    __tablename__ = 'courses'

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))

    course_name = Column(String, nullable=False, unique=True)
    grade = Column(Integer, nullable=False)

    subjects = relationship("Subject", back_populates="course")
    students = relationship("Student", back_populates="course")
    classes = relationship("SchoolClasse", back_populates="course")


# =========================
# ALUNOS
# =========================
class Student(Base):
    __tablename__ = 'students'

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))

    full_name = Column(String, nullable=False)
    course_id = Column(String, ForeignKey('courses.id'))
    class_id = Column(String, ForeignKey('classes.id'))
    gender = Column(String, nullable=False)
    birth_date = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    course = relationship("Course", back_populates="students")
    school_class = relationship("SchoolClasse", back_populates="students")
    frequencies = relationship("Frequency", back_populates="student")


# =========================
# PROFESSORES
# =========================
class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))

    user_id = Column(String, ForeignKey('users.id'))

    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="teacher")

    subjects = relationship("SubjectTeach", back_populates="teacher")


# =========================
# DISCIPLINAS
# =========================
class Subject(Base):
    __tablename__ = 'subjects'

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))

    subject_name = Column(String, nullable=False, unique=True)

    course_id = Column(String, ForeignKey('courses.id'))

    course = relationship("Course", back_populates="subjects")

    teachers = relationship("SubjectTeach", back_populates="subject")

    frequencies = relationship("Frequency", back_populates="subject")


# =========================
# TURMAS
# =========================
class SchoolClasse(Base):
    __tablename__ = 'classes'

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))

    name = Column(String, nullable=False)

    course_id = Column(String, ForeignKey('courses.id'))

    course = relationship("Course", back_populates="classes")

    students = relationship("Student", back_populates="school_class")


# =========================
# FREQUÊNCIA
# =========================
class Frequency(Base):
    __tablename__ = 'frequencies'

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))

    student_id = Column(String, ForeignKey('students.id'))

    subject_id = Column(String, ForeignKey('subjects.id'))

    presence = Column(Boolean, nullable=False)

    date = Column(DateTime, default=datetime.utcnow)

    student = relationship("Student", back_populates="frequencies")

    subject = relationship("Subject", back_populates="frequencies")


# =========================
# PROFESSOR <-> DISCIPLINA
# =========================
class SubjectTeach(Base):
    __tablename__ = 'subject_teach'

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))

    teacher_id = Column(String, ForeignKey('teachers.id'))

    subject_id = Column(String, ForeignKey('subjects.id'))

    teacher = relationship("Teacher", back_populates="subjects")

    subject = relationship("Subject", back_populates="teachers")