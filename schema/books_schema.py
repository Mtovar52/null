from pydantic import BaseModel

from typing import List, Optional


class Book(BaseModel):
    id: Optional[int]
    title: str
    subtitle: str
    author: str
    category: str
    publisher: str
    editor: str 
    description: str
    state: Optional[int]
    #publication_date: datetime 
 
class BookGoogle(BaseModel):
    id: Optional[str]
    title: str
    subtitle: str
    author: str
    category: str
    publisher: str
    editor: str 
    description: str
   