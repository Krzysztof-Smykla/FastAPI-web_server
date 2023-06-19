# schema.py
from pydantic import BaseModel


class StudentCreateSchema(BaseModel):
    first_name: str
    last_name: str
    email: str


class Student(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str


class StudentUpdateSchema(BaseModel):
    student_id: int
    first_name: str
    last_name: str
    email: str
