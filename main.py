from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(title = 'ToDo List')

data = [
    {
        'id' : 'aaaaa',
        'title': 'Estudar Python',
        'priority' : 1,
        'done': False 
    },
    {
        'id' : 'bbbbb',
        'title': 'Estudar PySpark',
        'priority' : 2,
        'done': False 
    },    
]

class Todo(BaseModel):
    title: str
    priority: str
    done: bool

@app.get('/')
def home():
    return {'ping': 'pong'}

@app.get('/todo')
def get_all():
    return data    

@app.get('/todo/{id}')    
def get(id: str)->Todo:
    
    todo = search_todo(id)

    return todo


@app.put('/todo/{todo_id}')
def update(todo_id:str, todo:Todo)->Todo:
    to_do = search_todo(todo_id=todo_id)

    if to_do:
        to_do['title'] = todo.title
        to_do['priority'] = todo.priority
        to_do['done'] = todo.done
        
        return to_do
    return {'message': 'ToDo not found'}

def search_todo(todo_id) -> dict | None:
    search = list(filter(lambda x: x["id"] == todo_id, data)) 

    if len(search) > 0:
        return search[0]