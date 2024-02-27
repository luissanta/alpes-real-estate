from fastapi import APIRouter, status
from app.moduls.lists.aplication.services import ListService
from app.moduls.lists.aplication.mappers import MapperListEstates as MapApp

list_router = APIRouter(
    tags=["list"]
)


@list_router.get("/list", status_code=status.HTTP_200_OK)
async def get_list():
    map_estates = MapApp()
    sr = ListService()
    return map_estates.dto_to_external(sr.get_list_entities())


 
