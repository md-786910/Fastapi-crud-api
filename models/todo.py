# check typing scripting

from pydantic import BaseModel


class Todo(BaseModel):
    title: str
    description: str


class CreateTodo(Todo):
    pass
        
        
class GetTodo(Todo):
    id:int
    
    class config:
        orm_mode = True
