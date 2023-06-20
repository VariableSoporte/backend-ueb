from fastapi import FastAPI
from routes import courses, students, dignities, candidates, lists, users, vote, students_new
from database import engine
import models

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(courses.course_router, prefix="/courses", tags=["courses"])
# app.include_router(students.student_router, prefix="/students", tags=["students"])
app.include_router(dignities.dignity_router, prefix="/dignities", tags=["dignities"])
app.include_router(candidates.candidate_router, prefix="/candidates", tags=["candidates"])
app.include_router(lists.list_router, prefix="/lists", tags=["lists"])
app.include_router(users.user_router, prefix="/users", tags=["users"])
app.include_router(vote.votes_router, prefix="/votes", tags=["votes"])
app.include_router(students_new.test_router, prefix="/students", tags=["students"])

