from fastapi import FastAPI
from typing import Optional
from Pydantic import BaseModel

class Blog(BaseModel):
    pass
# instance of the app
app =FastAPI()
# default path
@app.get('/blog') 
def index(limit=10,published:bool=True,sort:Optional[str]=None):
    # in local host it will return in json
    if published:
        return {'data':f'{limit} published blog list'}
    else:
         return {'data':f'{limit}  blog list'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpulish'}
# path
@app.get('/blog/{id}')
# defining the type
def  about(id:int):
    # fetecg blog with id =id
    return {'data':id}

@app.get('/blog/{id}/comments')
def comments(id):
    # fetch comments of block with id=id

    return {'data':{'1','2'}}
# craete
@app.post('/blog')
def create_blog(request:Blog):
    return {'data':'blog is created'}

