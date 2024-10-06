from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.tipo_pago.Tipo_pagoDao import Tipo_pagoDao

tipapi = Blueprint('tipapi', __name__)

# Trae todas las ciudades
@tipapi.route('/tipo_pagos', methods=['GET'])
def gettipo_pagos():
    tipdao = Tipo_pagoDao()

    try:
        tipo_pagos = tipdao.getTipo_pago()

        return jsonify({
            'success': True,
            'data': tipo_pagos,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todos los tipo_pagos: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@tipapi.route('/tipo_pagos/<int:tipo_pago_id>', methods=['GET'])
def getTipo_pago(tipo_pago_id):
    tipdao = Tipo_pagoDao()

    try:
        tipo_pago = tipdao.getTipo_pagoById(tipo_pago_id)

        if tipo_pago:
            return jsonify({
                'success': True,
                'data': tipo_pago,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el tipo_pago con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener el tipo_pago: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega una nueva ciudad
@tipapi.route('/tipo_pagos', methods=['POST'])
def addTipo_pago():
    data = request.get_json()
    tipdao = Tipo_pagoDao()

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
        tipo_pago_id = tipdao.guardarTipo_pago(descripcion)
        if tipo_pago_id is not None:
            return jsonify({
                'success': True,
                'data': {'id': tipo_pago_id, 'descripcion': descripcion},
                'error': None
            }), 201
        else:
            return jsonify({ 'success': False, 'error': 'No se pudo guardar el tipo_pago. Consulte con el administrador.' }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar el tipo_pago: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@tipapi.route('/tipo_pagos/<int:tipo_pago_id>', methods=['PUT'])
def updateTipo_pago(tipo_pago_id):
    data = request.get_json()
    tipdao = Tipo_pagoDao()

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
        if tipdao.updateTipo_pago(tipo_pago_id, descripcion.upper()):
            return jsonify({
                'success': True,
                'data': {'id':tipo_pago_id, 'descripcion': descripcion},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el tipo_pago con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar el tipo_pago: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@tipapi.route('/tipo_pagos/<int:tipo_pago_id>', methods=['DELETE'])
def deleteTipo_pago(tipo_pago_id):
    tipdao = Tipo_pagoDao()

    try:
        # Usar el retorno de eliminarCiudad para determinar el éxito
        if tipdao.deleteTipo_pago(tipo_pago_id):
            return jsonify({
                'success': True,
                'mensaje': f'tipo_pago con ID {tipo_pago_id} eliminada correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el tipo_pago con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar el tipo_pago: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500