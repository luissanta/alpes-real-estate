from fastapi import APIRouter, status
from app.moduls.lists.aplication.services import ListService
from app.moduls.lists.aplication.mappers import MapperListEstates

list_router = APIRouter(
    tags=["list"]
)


@list_router.get("/list", status_code=status.HTTP_200_OK)
async def get_list():
    map_estates = MapperListEstates()
    sr = ListService()
    return map_estates.dto_to_entity(sr.get_list_entities())


 
