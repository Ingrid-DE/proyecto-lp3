from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.paciente.PacienteDao import PacienteDao

pacapi = Blueprint('pacapi', __name__)

# Trae todas las ciudades
@pacapi.route('/pacientes', methods=['GET'])
def getPacientes():
    pacdao = PacienteDao()

    try:
        pacientes = pacdao.getPaciente()

        return jsonify({
            'success': True,
            'data': pacientes,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todos los pacientes: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@pacapi.route('/pacientes/<int:paciente_id>', methods=['GET'])
def getPaciente(paciente_id):
    pacdao = PacienteDao()

    try:
        paciente = pacdao.getPacienteById(paciente_id)

        if paciente:
            return jsonify({
                'success': True,
                'data': paciente,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró al paciente con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener paciente: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega una nueva ciudad
@pacapi.route('/pacientes', methods=['POST'])
def addPaciente():
    data = request.get_json()
    pacdao = PacienteDao()

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
        paciente_id = pacdao.guardarPaciente(descripcion)
        if paciente_id is not None:
            return jsonify({
                'success': True,
                'data': {'id': paciente_id, 'descripcion': descripcion},
                'error': None
            }), 201
        else:
            return jsonify({ 'success': False, 'error': 'No se pudo guardar al paciente. Consulte con el administrador.' }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar paciente: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@pacapi.route('/pacientes/<int:paciente_id>', methods=['PUT'])
def updatePaciente(paciente_id):
    data = request.get_json()
    pacdao = PacienteDao()

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
        if pacdao.updatePaciente(paciente_id, descripcion.upper()):
            return jsonify({
                'success': True,
                'data': {'id': paciente_id, 'descripcion': descripcion},
                'error': None
            }), 200
    
            return jsonify({
                'success': False,
                'error': 'No se encontró la ciudad con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar paciente: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@pacapi.route('/pacientes/<int:paciente_id>', methods=['DELETE'])
def deletePaciente(paciente_id):
    pacdao = PacienteDao()

    try:
        # Usar el retorno de eliminarCiudad para determinar el éxito
        if pacdao.deletePaciente(paciente_id):
            return jsonify({
                'success': True,
                'mensaje': f'Paciente con ID {paciente_id} eliminada correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró al paciente con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar paciente: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500