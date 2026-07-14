from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI,Depends, HTTPException
from contents import Notes
from database import SessionLocal, engine
from sqlalchemy.orm import Session
import databasemodel
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

print("Creating table.....")
databasemodel.Base.metadata.create_all(bind=engine)
print("Done")
@app.get("/Greet")
def greet():
    return "Hellooooo"

all_notes = [
    Notes(id = 1,name = "nishi",roll_no = 45,marks=90),
    Notes(id = 2,name = "hemmm",roll_no = 12,marks=96),
    Notes(id = 3,name = "sai",roll_no = 10,marks =98),
    
    Notes(id = 4,name = "laddu",roll_no = 13,marks=80)
]

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    db = SessionLocal()

    count = db.query(databasemodel.Notes).count()
    if count == 0:

        for note in all_notes:
            db.add(databasemodel.Notes(**note.model_dump()))
        db.commit()

init_db()

@app.get("/Products")
def get_all_products(db:Session = Depends(get_db)):
    db_products = db.query(databasemodel.Notes).all()

  
    return db_products
    
@app.get("/Products/{id}")
def get_Product_by_id(id: int,db:Session = Depends(get_db)):
    db_product = db.query(databasemodel.Notes).filter(databasemodel.Notes.id==id).first()
    if db_product:
        return db_product 
    return "Not found"


@app.post("/Add_product")
def add_product(note:Notes,db:Session = Depends(get_db)):
    new_note = databasemodel.Notes(**note.model_dump())
    db.add(new_note)
    db.commit()
    
    return "Added Successfullys"

@app.put("/updateProduct")
def update_product(id:int,note:Notes,db:Session = Depends(get_db)):
    db_product = db.query(databasemodel.Notes).filter(databasemodel.Notes.id==id).first()
    if db_product:
        db_product.name = note.name
        db_product.roll_no = note.roll_no
        db_product.marks = note.mark
        db.commit()
    else:
        return "No Product"


@app.delete("/Del")
def delete_student(id: int, db: Session = Depends(get_db)):
    student = db.query(databasemodel.Notes).filter(databasemodel.Notes.id == id).first()

    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    db.delete(student)
    db.commit()

    return {"message": "Student deleted"}
    

        






