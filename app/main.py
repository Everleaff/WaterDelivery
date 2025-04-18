from fastapi import FastAPI #.\venv\Scripts\activate ; uvicorn app.main:app ; uvicorn app.main:app --reload
from utils import json_to_dict_list
import os
from typing import Optional

path_to_json = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'students.json')

app = FastAPI()

@app.get("/students/{course}")
def get_all_students_course(course: int):
    students = json_to_dict_list(path_to_json)
    return_list = []
    for student in students:
        if student["course"] == course:
            return_list.append(student)
    return return_list