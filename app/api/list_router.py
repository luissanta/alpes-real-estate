from app.moduls.locations.aplication.commands.delete_location import DeleteLocation
import app.seedwork.presentation.apiflask as apiflask
import json
from typing import Any, Dict
from flask import redirect, render_template, request, session, url_for
from flask import Response, Request

from app.moduls.lists.aplication.querys.get_states import GetEstate
from app.moduls.lists.aplication.services import ListService
from app.moduls.lists.aplication.mappers import MapeadorEstateDTOJson as MapApp
from app.moduls.lists.aplication.commands.create_estate import CreateEstate
from app.moduls.lists.aplication.commands.delete_estate import DeleteEstate
from app.seedwork.domain.exceptions import DomainException

from app.seedwork.aplication.commands import execute_command
from app.seedwork.aplication.queries import execute_query

from app.moduls.locations.aplication.commands.create_location import CreateLocation

bp = apiflask.create_blueprint('list_router', '/list_router')

cons_mimetype = 'application/json'


# @bp.route("/list/<list_id>", methods=('GET',))
# def get_by_id(list_id):
#     map_estates = MapApp()
#     sr = ListService()
#     return map_estates.dto_to_external(sr.get_all_list())

@bp.route("/list", methods=('GET',))
def get_list():
    map_estates = MapApp()
    sr = ListService()
    result = map_estates.dto_to_external(sr.get_all_list())
    return result

@bp.route("/listQuery", methods=('GET',))
def get_estate_using_query(id=None):
    query_resultado = execute_query(GetEstate(id))
    map_estates = MapApp()
    
    return map_estates.dto_to_external(query_resultado.resultado)

@bp.route("/estate-command", methods=('POST',))
def async_create_estate():
    try:
        estate_dict = request.json

        #print("Request.json: ", estate_dict)
        map_estate = MapApp()
        estate_dto = map_estate.external_to_dto(estate_dict)

        command = CreateEstate(estate_dto)        
        command.data = estate_dict
        execute_command(command)
        
        return Response('{}', status=201, mimetype=cons_mimetype)
    except DomainException as e:
<<<<<<< HEAD
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

=======
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype=cons_mimetype)

@bp.route("/delete/<estate_id>", methods=('DELETE',))
def async_delete_estate(estate_id: str):
    try:
        command = DeleteEstate(estate_id)
        execute_command(command)
        return Response('{}', status=200, mimetype=cons_mimetype)
    except DomainException as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype=cons_mimetype)
>>>>>>> develop

@bp.route("/location-command", methods=('POST',))
def async_create_location():
    try:
        estate_dict = request.json

        #print("Request.json: ", estate_dict)
        map_estate = MapApp()
        estate_dto = map_estate.external_to_dto(estate_dict)

        command = CreateLocation(estate_dto)
        
<<<<<<< HEAD
        # TODO Reemplaze es todo código sincrono y use el broker de eventos para propagar este comando de forma asíncrona
        # Revise la clase Despachador de la capa de infraestructura
        execute_command(command)
        
        return Response('{}', status=201, mimetype='application/json')
    except DomainException as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
=======
        execute_command(command)
        
        return Response('{}', status=201, mimetype=cons_mimetype)
    except DomainException as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype=cons_mimetype)
    
@bp.route("/delete-locate/<location_id>", methods=('DELETE',))
def async_delete_location(location_id: str):
    try:
        command = DeleteLocation(location_id)
        execute_command(command)
        return Response('{}', status=200, mimetype=cons_mimetype)
    except DomainException as e:

        return Response(json.dumps(dict(error=str(e))), status=400, mimetype=cons_mimetype)    
>>>>>>> develop
