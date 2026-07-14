from pydantic import BaseModel

class Notes(BaseModel):
    id : int
    name : str
    roll_no: int
    marks : int

    

