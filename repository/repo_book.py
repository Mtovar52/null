from schema.books_schema import Book 
from fastapi import Response
from config.db import engine
from model.books import books
from starlette import status
import json
from typing import List

class Books_repository:

    def create_book(self, book:Book): #----------------- CREATE BOOK----------------
        new_book = books.insert().values(
                    title= book.title, 
                    subtitle=book.subtitle,
                    author=book.author,
                    category=book.category,
                    publisher=book.publisher,
                    editor=book.editor,
                    description=book.description,
                    state=1
                ) 
        try:
            with engine.connect() as conn:
                conn.execute(new_book)
                conn.commit()
                data = {"message": "Book create successfully","is_ok": True, "status_code": status.HTTP_201_CREATED}
                return Response(status_code=201,content=json.dumps(data), media_type="application/json")         
        except Exception as e:
            data = {"message": "Error saving book","is_ok": False, "status_code": status.HTTP_302_FOUND}
            return Response(status_code=302,content=json.dumps(data), media_type="application/json")
    

    def delete_book(self, ID:int): #----------------- DELETE BOOK -------------------       
        delete_book = books.update().where(books.c.id==ID, books.c.state==1).values(state=0) 
        try:
            with engine.connect() as conn:
                result = conn.execute(delete_book)
                if result.rowcount > 0:
                    conn.commit()
                    print("Book deleted successfully")
                elif result.rowcount == 0:
                    raise Exception
        except Exception as e:
            if result.rowcount == 0:
                print("Error Book not found", e) 

 
    def list_book(self): #----------------- LIST BOOK -------------------         
        try:
            with engine.connect() as conn:
                results = conn.execute(books.select()).fetchall()
                book_dict = []
                for result in results:
                    book_dict.append({
                        "id": result.id,
                        "title": result.title,
                        "author": result.author,
                        "subtitle": result.subtitle,
                        "category": result.category,
                        "publisher": result.publisher,
                        "editor": result.editor,
                        "description": result.description,
                        "state": result.state
                    })
                return book_dict
        except Exception as e:
            print("Error, books not found correctly", e)
            return []   

'''    def list_by_id(self): #----------------- LIST BOOK -------------------         
        try:
            with engine.connect() as conn:
                results = conn.execute(books.select()).fetchall()
                book_dict = []
                
                    (
                        "id": result.id,
                        "title": result.title,
                        "author": result.author,
                        "subtitle": result.subtitle,
                        "category": result.category,
                        "publisher": result.publisher,
                        "editor": result.editor,
                        "description": result.description,
                        "state": result.state
                    )
                return book_dict
        except Exception as e:
            print("Error, books not found correctly", e)
            return []   '''