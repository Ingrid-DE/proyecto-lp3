from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.servicio.ServicioDao import ServicioDao

serapi = Blueprint('serapi', __name__)

# Trae todas las ciudades
@serapi.route('/servicios', methods=['GET'])
def getServicios():
    serdao = ServicioDao()

    try:
        servicios = serdao.getServicios()

        return jsonify({
            'success': True,
            'data': servicios,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todos los servicios: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@serapi.route('/servicios/<int:servicio_id>', methods=['GET'])
def getServicio(servicio_id):
    serdao = ServicioDao()

    try:
        servicio = serdao.getServicioById(servicio_id)

        if servicio:
            return jsonify({
                'success': True,
                'data': servicio,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la ciudad con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener servicio: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega una nueva ciudad
@serapi.route('/servicios', methods=['POST'])
def addServicio():
    data = request.get_json()
    serdao = ServicioDao()

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
        servicio_id = serdao.guardarServicio(descripcion)
        if servicio_id is not None:
            return jsonify({
                'success': True,
                'data': {'id': servicio_id, 'descripcion': descripcion},
                'error': None
            }), 201
        else:
            return jsonify({ 'success': False, 'error': 'No se pudo guardar el servicio. Consulte con el administrador.' }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar servicio: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@serapi.route('/servicios/<int:servicio_id>', methods=['PUT'])
def updateServicio(servicio_id):
    data = request.get_json()
    serdao = ServicioDao()

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
        if serdao.updateServicio(servicio_id, descripcion.upper()):
            return jsonify({
                'success': True,
                'data': {'id': servicio_id, 'descripcion': descripcion},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la servicio con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar servicio: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@serapi.route('/servicios/<int:servicio_id>', methods=['DELETE'])
def deleteServicio(servicio_id):
    serdao = ServicioDao()

    try:
        # Usar el retorno de eliminarCiudad para determinar el éxito
        if serdao.deleteServicio(servicio_id):
            return jsonify({
                'success': True,
                'mensaje': f'Servicio con ID {servicio_id} eliminada correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el servicio con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar servicio: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500