from fastapi import FastAPI

app = FastAPI()

app.get('/')
async def root():
    return {'message': 'hello World'}

#this is broken, will not return "hello World"