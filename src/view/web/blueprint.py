from flask import Blueprint, render_template, request
import sys
sys.path.append("src")
from model.models import Empleado, Liquidacion
from controller import empleado_controller, liquidacion_controller

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

@blueprint.route('/crear_empleado')
def crear_empleado():
    data = {"nombre": request.args["nombre"],
            "documento": request.args["documento"],
            "salario_base": request.args["salario_base"],
            "fecha_ingreso": request.args["fecha_ingreso"]}
    
    resultado = empleado_controller.EmpleadoController.create(data)
    return render_template('crear_empleado.html', resultado=resultado)

@blueprint.route('/crear_liquidacion')
def crear_liquidacion():
    data = {"empleado_id": request.args["empleado_id"],
            "salario_base": request.args["salario_base"],
            "horas_diurnas": request.args["horas_diurnas"],
            "horas_nocturnas": request.args["horas_nocturnas"],
            "bonos_extra": request.args["bonos_extra"],
            "deduccion_adicional": request.args["deduccion_adicional"]}
    
    resultado = liquidacion_controller.LiquidacionController.create(data)
    return render_template('crear_liquidacion.html', resultado=resultado)

@blueprint.route('/borrar_empleado')
def borrar_empleado():
    id = request.args["id"]
    resultado = empleado_controller.EmpleadoController.delete(id)
    return render_template('borrar_empleado.html', resultado=resultado)

@blueprint.route('/borrar_liquidacion')
def borrar_liquidacion():
    id = request.args["id"]
    resultado = liquidacion_controller.LiquidacionController.delete(id)
    return render_template('borrar_liquidacion.html', resultado=resultado)