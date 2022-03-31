from fastapi import FastAPI
from db.database import engine, Base, SessionLocal
from models import Project

Base.metadata.create_all(bind=engine)
app = FastAPI()


def get_db():
    """
    每一个请求处理完毕后会关闭当前连接，不同的请求使用不同的连接
    :return:
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/add-project')
async def create_item(project: Project):
    return project.symbol
