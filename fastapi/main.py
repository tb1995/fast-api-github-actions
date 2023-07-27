from typing import Union
from config import db_conn, db_engine
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()


class User(BaseModel):
    name: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/users", response_model=User)
def create_users(user: User):

    user_name = user.name

    cur = db_conn.cursor()
    insert_user_query = f"""
    
"""
    cur.execute(
        "INSERT INTO users (name) VALUES (%s) RETURNING id", (user_name,))
    user_id = cur.fetchone()[0]
    db_conn.commit()

    return {"id": user_id, "name": user_name}


@app.get("/users")
def get_users():
    cur = db_conn.cursor()
    get_user_query = f"""
    SELECT * FROM users;
    """
    cur.execute(get_user_query)
    users = cur.fetchall()

    return users


@app.get("/health")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
