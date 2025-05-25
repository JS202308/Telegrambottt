from typing import List

from pydantic import BaseModel


class FilmModel(BaseModel):
    name: str
    rating: float
    description: str
    genre: str
    actors: List[str]
    poster: str