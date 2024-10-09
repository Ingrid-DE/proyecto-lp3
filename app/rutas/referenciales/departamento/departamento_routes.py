from flask import Blueprint, render_template

deptmod = Blueprint('departamento', __name__, template_folder='templates')

@deptmod.route('/departamento-index')
def departamentoIndex():
    return render_template('departamento-index.html')