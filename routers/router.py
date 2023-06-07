from fastapi import APIRouter, Response
from schema.books_schema import Book 
from starlette import status
from repository.repo_book import Books_repository
from typing import List

router = APIRouter()

@router.get("/")
async def boots():
    return {"Hello": "Welcome to bibliothek"}

@router.post("/books")
async def create_book(data_book: Book):
    repository = Books_repository()
    result=repository.create_book(data_book)
    return result
    
@router.delete("/books/{id}")
async def delete_book(id: int):
    repository = Books_repository()
    repository.delete_book(id)
    
@router.get("/books", response_model=List[Book])
def get_books():
    repository = Books_repository()
    result=repository.list_book()
    return result

'''@router.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    return {"message": "Book not found"}

    '''
