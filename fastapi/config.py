import os
import dotenv
from sqlalchemy import create_engine
import psycopg2

# load .env.local
dotenv.load_dotenv(dotenv.find_dotenv(filename=".env"))


db_config = {
    "database": os.environ.get("DB_NAME", "mobilitydb"),
    "user": os.environ.get("DB_USER", "postgres"),
    "password": os.environ.get("DB_PASS", "postgres"),
    "host": os.environ.get("DB_HOST", "db"),
    "port": os.environ.get("DB_PORT", "5432"),
    "aws_access_key_id": os.environ.get("AWS_ACCESS_KEY_ID", ""),
    "aws_secret_access_key": os.environ.get("AWS_SECRET_ACCESS_KEY", ""),
}

db_conn = psycopg2.connect(
    database=db_config["database"],
    user=db_config["user"],
    password=db_config["password"],
    host=db_config["host"],
    port=db_config["port"],
)
db_conn.autocommit = True
db_engine = create_engine(
    f"postgresql+psycopg2://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}"
)
# Path: config.py
