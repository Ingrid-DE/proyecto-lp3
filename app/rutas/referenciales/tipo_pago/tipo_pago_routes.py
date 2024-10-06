from flask import Blueprint,render_template

tipmod = Blueprint('tipo_pago', __name__, template_folder='templates')

@tipmod.route('/tipo_pago-index')
def tipo_pagoIndex():
    return render_template('tipo_pago-index.html')