# -*- coding: utf-8 -*-

from flask_restful import Resource, reqparse, marshal_with
from flask_restful_swagger import swagger
from app.mod_shared.models import db
from app.mod_profiles.models import *
from app.mod_profiles.resources.fields.profileFields import ProfileFields

parser = reqparse.RequestParser()
parser.add_argument('last_name', type=str, required=True)
parser.add_argument('first_name', type=str, required=True)
parser.add_argument('gender_id', type=int)
parser.add_argument('birthday')

class ProfileView(Resource):
    @swagger.operation(
        notes=u'Retorna una instancia específica de perfil.'.encode('utf-8'),
        responseClass='ProfileFields',
        nickname='profileView_get',
        parameters=[
            {
              "name": "id",
              "description": u'Identificador único del perfil.'.encode('utf-8'),
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
    @marshal_with(ProfileFields.resource_fields, envelope='resource')
    def get(self, id):
        profile = Profile.query.get_or_404(id)
        return profile

    @swagger.operation(
        notes=u'Actualiza una instancia específica de perfil, y la retorna.'.encode('utf-8'),
        responseClass='ProfileFields',
        nickname='profileView_put',
        parameters=[
            {
              "name": "id",
              "description": u'Identificador único del perfil.'.encode('utf-8'),
              "required": True,
              "dataType": "int",
              "paramType": "path"
            },
            {
              "name": "last_name",
              "description": u'Apellido de la persona.'.encode('utf-8'),
              "required": True,
              "dataType": "string",
              "paramType": "body"
            },
            {
              "name": "first_name",
              "description": u'Nombre de la persona.'.encode('utf-8'),
              "required": True,
              "dataType": "string",
              "paramType": "body"
            },
            {
              "name": "birthday",
              "description": u'Fecha de nacimiento de la persona, en formato ISO 8601.'.encode('utf-8'),
              "required": False,
              "dataType": "datetime",
              "paramType": "body"
            },
            {
              "name": "gender_id",
              "description": u'Identificador único del género asociado.'.encode('utf-8'),
              "required": False,
              "dataType": "int",
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
    @marshal_with(ProfileFields.resource_fields, envelope='resource')
    def put(self, id):
        profile = Profile.query.get_or_404(id)
        args = parser.parse_args()

        # Actualiza los atributos y relaciones del objeto, en base a los
        # argumentos recibidos.

        # Actualiza el apellido, en caso de que haya sido modificado.
        if (args['last_name'] is not None and
              profile.last_name != args['last_name']):
            profile.last_name = args['last_name']
        # Actualiza el nombre, en caso de que haya sido modificado.
        if (args['first_name'] is not None and
              profile.first_name != args['first_name']):
            profile.first_name = args['first_name']
        # Actualiza el genero, en caso de que haya sido modificado.
        if (args['gender_id'] is not None and
              profile.gender_id != args['gender_id']):
            profile.gender_id = args['gender_id']
        # Actualiza la fecha de nacimiento, en caso de que haya sido
        # modificada.
        if (args['birthday'] is not None and
              profile.birthday != args['birthday']):
            profile.birthday = args['birthday']

        db.session.commit()
        return profile, 200