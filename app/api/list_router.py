from fastapi import APIRouter, status
from app.moduls.lists.aplication.querys.get_states import GetEstate
from app.moduls.lists.aplication.services import ListService
from app.moduls.lists.aplication.mappers import MapeadorEstateDTOJson as MapApp
from app.seedwork.aplication.queries import ejecutar_query

list_router = APIRouter(
    tags=["list"]
)


@list_router.get("/list", status_code=status.HTTP_200_OK)
async def get_list():
    map_estates = MapApp()
    sr = ListService()
    return map_estates.dto_to_external(sr.get_all_list())

@list_router.get("/listQuery", status_code=status.HTTP_200_OK)
def dar_reserva_usando_query(id=None):
    query_resultado = ejecutar_query(GetEstate(id))
    map_reserva = MapApp()
    
    return map_reserva.dto_to_external(query_resultado.resultado)