# -*- coding: utf-8 -*-

from flask_restful import Resource, reqparse, marshal_with
from flask_restful_swagger import swagger
from app.mod_shared.models import db
from app.mod_profiles.models import *
from app.mod_profiles.resources.fields.measurementSourceFields import MeasurementSourceFields

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True)
parser.add_argument('description', type=str)

class MeasurementSourceView(Resource):
    @swagger.operation(
        notes=u'Retorna una instancia específica de fuente de medición.'.encode('utf-8'),
        responseClass='MeasurementSourceFields',
        nickname='measurementSourceView_get',
        parameters=[
            {
              "name": "id",
              "description": u'Identificador único de la fuente de medición.'.encode('utf-8'),
              "required": True,
              "dataType": "int",
              "paramType": "path"
            }
          ],
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
    @marshal_with(MeasurementSourceFields.resource_fields, envelope='resource')
    def get(self, id):
        measurement_source = MeasurementSource.query.get_or_404(id)
        return measurement_source

    @swagger.operation(
        notes=u'Actualiza una instancia específica de fuente de medición, y la retorna.'.encode('utf-8'),
        responseClass='MeasurementSourceFields',
        nickname='measurementSourceView_put',
        parameters=[
            {
              "name": "id",
              "description": u'Identificador único de la fuente de medición.'.encode('utf-8'),
              "required": True,
              "dataType": "int",
              "paramType": "path"
            },
            {
              "name": "name",
              "description": u'Nombre de la fuente de medición.'.encode('utf-8'),
              "required": True,
              "dataType": "string",
              "paramType": "body"
            },
            {
              "name": "description",
              "description": u'Descripción de la fuente de medición.'.encode('utf-8'),
              "required": False,
              "dataType": "string",
              "paramType": "body"
            }
          ],
        responseMessages=[
            {
              "code": 200,
              "message": "Objeto actualizado exitosamente."
            },
            {
              "code": 404,
              "message": "Objeto inexistente."
            }
          ]
        )
    @marshal_with(MeasurementSourceFields.resource_fields, envelope='resource')
    def put(self, id):
        measurement_source = MeasurementSource.query.get_or_404(id)
        args = parser.parse_args()

        # Actualiza los atributos y relaciones del objeto, en base a los
        # argumentos recibidos.

        # Actualiza el nombre, en caso de que haya sido modificado.
        if (args['name'] is not None and
              measurement_source.name != args['name']):
            measurement_source.name = args['name']
        # Actualiza la descripcion, en caso de que haya sido modificada.
        if (args['description'] is not None and
              measurement_source.description != args['description']):
            measurement_source.description = args['description']

        db.session.commit()
        return measurement_source, 200