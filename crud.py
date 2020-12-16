from sqlalchemy.orm import Session
import models, schemas

#CRUD Functions
def get_users_by_id(db : Session , user_id : int) :
    #get users by ID
    return db.query(models.users).filter(models.users.id == user_id).first()

def get_users_by_name(db : Session , user_name : str) :
    #get users by name
    #fetch the first model with matching name 
    return db.query(models.users).filter(models.users.name == user_name).first()

def create_user(db: Session, user_name: str):
    #create user and commit into db
    #return the model
    db_user = models.users(name = user_name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id : int):
    #fetch model,  delete user and commit into db
    #return status of sucess of failure
    if(instance := get_users_by_id(db = db , user_id = user_id )) is  None : 
        return False 
    db.delete(instance)
    db.commit()
    return True

def update_user(db: Session, user_id : int , user_name : str):
    #fetch model, update and commit into db
    #return status of sucess of failure
    #if sucessful return the model
    if(instance := get_users_by_id(db = db , user_id = user_id )) is  None : 
        return False 
    instance.name = user_name
    db.commit()
    return instance 
