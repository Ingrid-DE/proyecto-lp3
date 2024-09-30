from flask import Flask

app = Flask(__name__)

# importar referenciales
from app.rutas.referenciales.ciudad.ciudad_routes import ciumod 
from app.rutas.referenciales.persona.persona_routes import permod
from app.rutas.referenciales.medico.medico_routes import medmod

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

# APIS v1
version1 = '/api/v1'
app.register_blueprint(ciuapi, url_prefix=version1)

version1 = '/api/v1'
app.register_blueprint(perapi, url_prefix=version1)

version1 = '/api/v1'
app.register_blueprint(medapi, url_prefix=version1)