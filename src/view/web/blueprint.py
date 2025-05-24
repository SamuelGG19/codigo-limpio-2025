from flask import Blueprint, render_template, request
import sys
sys.path.append("src")
from model.models import Empleado, Liquidacion

blueprint = Blueprint("blueprint", __name__, "templates")

@blueprint.route('/')
def main():
    return render_template('main.html')#, option=request.args["option"])

@blueprint.route('/enviar')
def enviar():
    return render_template('enviar.html', option=request.args["option"])

@blueprint.route('/lista_empleados')
def lista_empleados():
    documento = request.args["documento"]
    resultado = Empleado.get_by_documento(documento)
    return render_template('lista_empleados.html', documento=documento, empleado=resultado)

@blueprint.route('/lista_liquidaciones')
def lista_liquidaciones():
    id = request.args["id_empleado"]
    resultado = Liquidacion.get_by_empleado(id)
    return render_template('lista_liquidaciones.html', id_empleado=id, liquidaciones=resultado)