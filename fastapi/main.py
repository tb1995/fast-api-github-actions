from typing import Union
from config import db_conn, db_engine
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    # allow_origins=origins,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class User(BaseModel):
    name: str


@app.get("/test/setup")
def read_root():
    cur = db_conn.cursor()
    cur.execute("DROP TABLE IF EXISTS users;")

    cur.execute("""CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
    );""")
    return {"Hello": "World"}


@app.post("/users", response_model=User)
def create_users(user: User):

    user_name = user.name

    cur = db_conn.cursor()

    db_conn.commit()

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
