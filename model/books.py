from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, meta_data

books = Table(
    'books', meta_data,
    Column('id', Integer, primary_key=True),
    Column('title', String(255), nullable=False),
    Column('subtitle', String(255), nullable=False),
    Column('author', String(255), nullable=False),
    Column('category', String(255), nullable=False),
    Column('publisher', String(255), nullable=False),
    Column('editor', String(255), nullable=False),
    Column('description', String(255), nullable=False),
    Column('state', Integer, nullable=False)
    #Column('publication_date', DateTime, nullable=False)
)

meta_data.create_all(engine)