from typing import ClassVar

from app.schemas.base import CreateBase, InDBBase, ResponseBase, UpdateBase

class RestaurantCreate(CreateBase):
    name: str
    address: str
    latitude: float
    longitude: float
    cuisine: str
    average_rating: float
    created_at: str


class RestaurantUpdate(UpdateBase):
    name: str
    address: str
    latitude: float
    longitude: float
    cuisine: str
    average_rating: float
    created_at: str

class Restaurant(ResponseBase):
    name: str
    address: str
    latitude: float
    longitude: float
    cuisine: str
    average_rating: float
    created_at: str
    table_name: ClassVar[str] = "restaurant"

class RestaurantInDB(InDBBase):
    name: str
    address: str
    latitude: float
    longitude: float
    cuisine: str
    average_rating: float
    created_at: str


