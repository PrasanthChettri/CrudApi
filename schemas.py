from pydantic import BaseModel

class users_in(BaseModel):
    id : int 
    name : str

class users_in_name(BaseModel):
    name: str

class users_in_id(BaseModel):
    id : int 

class users_out(BaseModel):
    id : int 
    name : str