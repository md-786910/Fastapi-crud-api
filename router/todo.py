# model for -> pyandantic
#schema for -> sqlalchemy

import fastapi
from typing import List
from fastapi import Depends,status,HTTPException

from sqlalchemy.orm import Session

from db.connection import get_db,engine
from models.todo import GetTodo,CreateTodo
from schemas import todo

# model binds
todo.Base.metadata.create_all(bind=engine)


router = fastapi.APIRouter(
    tags=["Todo"],
)

@router.post("/create",status_code=status.HTTP_201_CREATED)
def create(item: CreateTodo, db:Session = Depends(get_db)):
    db_item = todo.Todo(**item.dict())
    if db_item:
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
    
    return {
        "message":"field are required"
    }

# get todo
@router.get("/getTodo",status_code=status.HTTP_200_OK,response_model=List[GetTodo])
def get_todo(db:Session = Depends(get_db)):
    todo_item = db.query(todo.Todo).all()
    return todo_item


# delete

@router.delete("/deleteTodo/{item_id}")
def get_todo(item_id:int,db:Session = Depends(get_db)):
    print(item_id)
    todo_item = db.query(todo.Todo).filter(todo.Todo.id == item_id).first()
    print(todo_item)
    if todo_item:
        db.delete(todo_item)
        db.commit()
        raise HTTPException(status_code=204,detail="successfully deleted item")
    
    raise HTTPException(status_code=404,detail="id not found ")

# update
@router.put("/updateTodo/{item_id}",status_code=status.HTTP_201_CREATED)
def create(item_id:int,item: CreateTodo, db:Session = Depends(get_db)):
    db_item = todo.Todo(**item.dict())

    todo_item = db.query(todo.Todo).filter(todo.Todo.id == item_id).first()
    todo_item.title = db_item.title
    todo_item.description = db_item.description
    db.commit()
    
    # if db_item:
    #     db.add(db_item)
    #     db.refresh(db_item)
    #     return db_item
    
    return {
        "message":"updated "
    }


@router.get("/get/{item_id}",status_code=status.HTTP_200_OK)
def get_todo(item_id: int, db:Session= Depends(get_db)):
    todo_item = db.query(todo.Todo).filter(todo.Todo.id==item_id).first()
    print(todo_item)
    if  todo_item:
        return {
            "todo":todo_item,
            "success":True
        }
        
    return {
        "message":"id does not exist",
    }    