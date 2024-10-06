from flask import Flask

app = Flask(__name__)

# importar referenciales
from app.rutas.referenciales.ciudad.ciudad_routes import ciumod 
from app.rutas.referenciales.persona.persona_routes import permod
from app.rutas.referenciales.medico.medico_routes import medmod
from app.rutas.referenciales.paciente.paciente_routes import pacmod
from app.rutas.referenciales.servicio.servicio_routes import sermod
from app.rutas.referenciales.ocupacion.ocupacion_routes import ocumod
from app.rutas.referenciales.turno.turno_routes import turmod
from app.rutas.referenciales.estado_civil.estado_civil_routes import estmod
from app.rutas.referenciales.pais.pais_routes import paimod
from app.rutas.referenciales.enfermedad.enfermedad_routes import enfmod

# registrar referenciales
modulo0 = '/referenciales'
app.register_blueprint(ciumod, url_prefix=f'{modulo0}/ciudad')

from app.rutas.referenciales.ciudad.ciudad_api import ciuapi


modulo0 = '/referenciales'
app.register_blueprint(permod, url_prefix=f'{modulo0}/persona')

from app.rutas.referenciales.persona.persona_api import perapi

modulo0 = '/referenciales'
app.register_blueprint(medmod, url_prefix=f'{modulo0}/medico')

from app.rutas.referenciales.medico.medico_api import medapi

modulo0 = '/referenciales'
app.register_blueprint(pacmod, url_prefix=f'{modulo0}/paciente')

from app.rutas.referenciales.paciente.paciente_api import pacapi

modulo0 = '/referenciales'
app.register_blueprint(sermod, url_prefix=f'{modulo0}/servicio')

from app.rutas.referenciales.servicio.servicio_api import serapi

modulo0 = '/referenciales'
app.register_blueprint(ocumod, url_prefix=f'{modulo0}/ocupacion')

from app.rutas.referenciales.ocupacion.ocupacion_api import ocuapi

modulo0 = '/referenciales'
app.register_blueprint(turmod, url_prefix=f'{modulo0}/turno')

from app.rutas.referenciales.turno.turno_api import turapi

modulo0 = '/referenciales'
app.register_blueprint(estmod, url_prefix=f'{modulo0}/estado_civil')

from app.rutas.referenciales.estado_civil.estado_civil_api import estapi

modulo0 = '/referenciales'
app.register_blueprint(paimod, url_prefix=f'{modulo0}/pais')

from app.rutas.referenciales.pais.pais_api import paiapi

modulo0 = '/referenciales'
app.register_blueprint(enfmod, url_prefix=f'{modulo0}/enfermedad')

from app.rutas.referenciales.enfermedad.enfermedad_api import enfapi

# APIS v1
version1 = '/api/v1'
app.register_blueprint(ciuapi, url_prefix=version1)

app.register_blueprint(perapi, url_prefix=version1)

app.register_blueprint(medapi,url_prefix=version1)

app.register_blueprint(pacapi, url_prefix=version1)

app.register_blueprint(serapi, url_prefix=version1)

app.register_blueprint(ocuapi, url_prefix=version1)

app.register_blueprint(turapi, url_prefix=version1)

app.register_blueprint(estapi, url_prefix=version1)

app.register_blueprint(paiapi, url_prefix=version1)

app.register_blueprint(enfapi, url_prefix=version1)