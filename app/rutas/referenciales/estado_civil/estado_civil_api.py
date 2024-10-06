from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.estado_civil.Estado_civilDao import Estado_civilDao

estapi = Blueprint('estapi', __name__)

# Trae todas las ciudades
@estapi.route('/estado_civiles', methods=['GET'])
def getEstado_civiles():
    estdao = Estado_civilDao()

    try:
        estado_civiles = estdao.getEstado_civiles()

        return jsonify({
            'success': True,
            'data': estado_civiles,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todos los estado_civiles: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@estapi.route('/estado_civiles/<int:estado_civil_id>', methods=['GET'])
def getEstado_civil(estado_civil_id):
    estdao = Estado_civilDao()

    try:
        estado_civil = estdao.getEstado_civilById(estado_civil_id)

        if estado_civil:
            return jsonify({
                'success': True,
                'data': estado_civil,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró al medico con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener estado_civiles: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega una nueva ciudad
@estapi.route('/estado_civiles', methods=['POST'])
def addestado_civil():
    data = request.get_json()
    estdao = Estado_civilDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['descripcion']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                            'success': False,
                            'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
                            }), 400

    try:
        descripcion = data['descripcion'].upper()
        estado_civil_id = estdao.guardarEstado_civil(descripcion)
        if estado_civil_id is not None:
            return jsonify({
                'success': True,
                'data': {'id': estado_civil_id, 'descripcion': descripcion},
                'error': None
            }), 201
        else:
            return jsonify({ 'success': False, 'error': 'No se pudo guardar el estado_civil. Consulte con el administrador.' }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar estado_civil: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@estapi.route('/estado_civiles/<int:estado_civil_id>', methods=['PUT'])
def updateEstado_civil(estado_civil_id):
    data = request.get_json()
    estdao = Estado_civilDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['descripcion']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                            'success': False,
                            'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
                            }), 400
    descripcion = data['descripcion']
    try:
        if estdao.updateEstado_civil(estado_civil_id, descripcion.upper()):
            return jsonify({
                'success': True,
                'data': {'id':estado_civil_id, 'descripcion': descripcion},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró al estado_civil con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar estado_civil: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@estapi.route('/estado_civiles/<int:estado_civil_id>', methods=['DELETE'])
def deleteEstado_civil(estado_civil_id):
    estdao = Estado_civilDao()

    try:
        # Usar el retorno de eliminarCiudad para determinar el éxito
        if estdao.deleteEstado_civil(estado_civil_id):
            return jsonify({
                'success': True,
                'mensaje': f'estado_civil con ID {estado_civil_id} eliminada correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró al estado_civil con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar estado_civil: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500