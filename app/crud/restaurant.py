from supabase import Client

from app.crud.base import CRUDBase
from app.schemas.restaurant import Restaurant, RestaurantCreate, RestaurantUpdate
from app.schemas.auth import UserIn

class CRUDRestaurant(CRUDBase[Restaurant, RestaurantCreate, RestaurantUpdate]):
    async def get(self, db: Client, *, id: str) -> Restaurant | None:
        """get by table_name by id"""
        return await super().get(db, id=id)

    async def get_all(self, db: Client) -> list[Restaurant]:
        """get all by table_name"""
        return await super().get_all(db)

    async def get_by_location(self, db: Client, location: tuple[float, float]) -> list[Restaurant]:
        """get by location"""
        pass
    
    async def get_by_cuisine(self, db: Client, cuisine: str) -> list[Restaurant]:
        """get by cuisine"""
    
    async def create(self, db: Client, *, obj_in: RestaurantCreate, user: UserIn) -> Restaurant:
        """create by CreateSchemaType"""
        pass

    async def update(self, db: Client, *, obj_in: RestaurantUpdate) -> Restaurant:
        """update by UpdateSchemaType"""
        pass

    async def delete(self, db: Client, *, id: str) -> Restaurant:
        pass


restaurant = CRUDRestaurant(Restaurant)
