from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/user')
async def user(
        *,
        user_id: int = Query(..., title="The ID of the user to get", gt=0)
):
    return {'user_id': user_id}
