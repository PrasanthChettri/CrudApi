from typing import List
from fastapi import Depends, FastAPI, HTTPException 
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine
from helper import ResponseModel
app = FastAPI()


models.Base.metadata.create_all(bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/get/id/{user_id}" , response_model=schemas.users_out)
def get_item_from_id(user_id : int , db: Session = Depends(get_db)):
    user = crud.get_users_by_id(db ,  user_id=user_id) 
    if (user := crud.get_users_by_id(db ,  user_id =user_id)) is None  : 
        raise HTTPException(status_code=404, detail="User not found")
    else :
        schema_obj = schemas.users_out(id = user.id , name = user.name)
        return schema_obj


@app.get("/get/name/{user_name}" , response_model=schemas.users_out)
def get_item_from_name(user_name : str , db: Session = Depends(get_db)):
    if (user := crud.get_users_by_name(db ,  user_name =user_name)) is None  : 
        raise HTTPException(status_code=404, detail="User not found")
    else :
        schema_obj = schemas.users_out(id = user.id , name = user.name)
        return schema_obj


@app.post("/post/"  , response_model=schemas.users_out)
def create_user(user : schemas.users_in_name , db: Session = Depends(get_db)):
    model_obj = crud.create_user(db = db , user_name = user.name)
    schema_obj = schemas.users_out(id = model_obj.id , name = model_obj.name)
    return schema_obj

@app.delete("/delete/")
def delete_user(user : schemas.users_in_id , db: Session = Depends(get_db)):
    deleted_user = crud.delete_user(db =db , user_id = user.id)
    if deleted_user:
        return ResponseModel(
            f"Student with ID: {user.id} removed" ,
            "Student deleted successfully"
        )
    else :
        raise HTTPException(status_code=404, detail="User not found")

@app.put("/update/" , response_model=schemas.users_out)
def update_student_data(user : schemas.users_in , db: Session = Depends(get_db)):
    updated_student = crud.update_user(db =db , user_id = user.id , user_name = user.name)
    if updated_student :
        schema_obj = schemas.users_out(id = updated_student.id , name = updated_student.name)
        return schema_obj
    else :
        raise HTTPException(status_code=404, detail="User not found")
