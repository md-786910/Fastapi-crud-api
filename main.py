import fastapi

# import router single
from router import todo 



app = fastapi.FastAPI()


# get router for testing
@app.get('/')
async def get_router():
    return "server Working fine"

app.include_router(todo.router)




