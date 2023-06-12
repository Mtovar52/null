from pydantic import BaseModel, validator
from typing import Optional


class Book(BaseModel):
    id: Optional[int]
    title: str
    subtitle: str
    author: str
    category: str
    publisher: str 
    description: str
    state: Optional[int]

    ##### no compatible con python 3.9xxx 
    @validator('title', 'subtitle', 'author', 'category', 'publisher', 'description')
    def validate_str_fields(cls, value):
        if not isinstance(value, str):
            raise ValueError('The field must be a string')
        return value