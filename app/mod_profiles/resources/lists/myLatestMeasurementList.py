# -*- coding: utf-8 -*-

from flask import g
from flask_restful import Resource, marshal_with
from flask_restful_swagger import swagger
from app.mod_shared.models.auth import auth
from app.mod_profiles.common.persistence import measurement
from app.mod_profiles.resources.fields.measurementFields import MeasurementFields


class MyLatestMeasurementList(Resource):
    # Crea una copia de los campos del recurso 'MeasurementView'.
    resource_fields = MeasurementFields.resource_fields.copy()
    # Quita el perfil asociado de los campos del recurso.
    del resource_fields['profile']

    @swagger.operation(
        # TODO: Añadir parámetros de autenticación a la documentación Swagger.
        notes= (u'Retorna la última instancia de medición de cada tipo de '
                'medición, asociadas al perfil del usuario autenticado.').encode('utf-8'),
        responseClass='MeasurementFields',
        nickname='myLatestMeasurementList_get',
        responseMessages=[
            {
              "code": 200,
              "message": "Objeto encontrado."
            },
            {
              "code": 404,
              "message": "Objeto inexistente."
            }
          ]
        )
    @auth.login_required
    @marshal_with(resource_fields, envelope='resource')
    def get(self):
        # Obtiene el perfil.
        profile = g.user.profile

        # Obtiene las últimas mediciones asociadas al perfil.
        latest_measurements = measurement.get_latest_by_profile(profile)
        return latest_measurements