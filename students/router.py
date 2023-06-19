# router.py
from fastapi import APIRouter, HTTPException
from .schema import StudentCreateSchema, Student, StudentUpdateSchema
from .storage import STUDENTS

router = APIRouter()


@router.get("/")
async def get_students():
    return STUDENTS


@router.post("/")
async def create_student(student: StudentCreateSchema):
    first_name = student.first_name
    last_name = student.last_name
    id = len(STUDENTS) + 1
    new_student = Student(**student.dict(), id=id)
    STUDENTS.append(new_student)
    return new_student


@router.get("/{student_id}")
async def read_item(student_id: int):
    if student_id not in [student.id for student in STUDENTS]:
        raise HTTPException(status_code=404, detail="Student not found")
    student = next(student for student in STUDENTS if student.id == student_id)
    return {"Student ID": student}


@router.delete("/{student_id}")
async def remove_student(student_id: int):
    for student in STUDENTS:
        if student.id == student_id:
            STUDENTS.remove(student)
            return {"message": f"Student with ID {student_id} has been removed."}
    raise HTTPException(status_code=404, detail="Student not found")


@router.put("/{student_id}")
async def update_student(student_id: int, updated_student: StudentUpdateSchema):
    if student_id not in [student.id for student in STUDENTS]:
        raise HTTPException(status_code=404, detail="Student not found")
    for student in STUDENTS:
        if student.id == student_id:
            student.first_name = updated_student.first_name
            student.last_name = updated_student.last_name
            student.email = updated_student.email
            return {"message": f"Student with ID {student_id} has been updated."}
    raise HTTPException(status_code=404, detail="Student not found")
