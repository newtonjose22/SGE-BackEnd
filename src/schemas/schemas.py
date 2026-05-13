from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime, date
from typing import Optional, List


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    cellphone: str
    role: str
    status: bool = True


class UserResponse(BaseModel):
    id: str
    name: str
    email: EmailStr
    cellphone: str
    role: str
    status: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)



class CourseCreate(BaseModel):
    course_name: str
    grade: int


class CourseResponse(CourseCreate):
    id: str

    model_config = ConfigDict(from_attributes=True)



class SchoolClasseCreate(BaseModel):
    name: str
    course_id: str


class SchoolClasseResponse(SchoolClasseCreate):
    id: str

    model_config = ConfigDict(from_attributes=True)




class StudentCreate(BaseModel):
    full_name: str
    course_id: str
    class_id: str
    gender: str
    birth_date: date


class StudentResponse(StudentCreate):
    id: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)



class TeacherCreate(BaseModel):
    user_id: str


class TeacherResponse(BaseModel):
    id: str
    user_id: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)





class SubjectCreate(BaseModel):
    subject_name: str
    course_id: str

class SubjectResponse(SubjectCreate):
    id: str

    model_config = ConfigDict(from_attributes=True)



class FrequencyCreate(BaseModel):
    student_id: str
    subject_id: str
    presence: bool

class FrequencyResponse(FrequencyCreate):
    id: str
    date: datetime

    model_config = ConfigDict(from_attributes=True)




class SubjectTeachCreate(BaseModel):
    teacher_id: str
    subject_id: str

class SubjectTeachResponse(SubjectTeachCreate):
    id: str

    model_config = ConfigDict(from_attributes=True)