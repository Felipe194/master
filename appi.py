from trabajadores import trabajadores
import string
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def hola():
    return "grupo 3-B"


@app.route('/personal')
def personalLista():
    return jsonify({"message": "PersonalUide"})


@app.route('/trabajadores', methods=['GET'])
def getTrabajador():
    return jsonify(trabajadores)

# BUSCA POR MATERIA


@app.route('/trabajadores/<string:materia_trabajador>', methods=['GET'])
def getrabajadores(materia_trabajador):
    listat = [
        tr for tr in trabajadores if tr["materia"] == materia_trabajador.lower()]
    if (len(listat) > 0):
        return jsonify({"trabajadores": listat[0]})
    return jsonify({"message": "Materia no encontrada"})


@app.route('/trabajadores', methods=['POST'])
def addTrabajador():
    # print(request.json)
    new_trabajador = {
        "id": request.json['id'],
        "name": request.json['name'],
        "apellido": request.json['apellido'],
        "cedula": request.json['cedula'],
        "materia": request.json['materia'],
        "titulos": request.json['titulos'],
        "pais": request.json['pais'],
        "ciudad": request.json['ciudad'],
    }
    trabajadores.append(new_trabajador)
    # return 'recibido'
    return jsonify({"message": "trabajador agregado", 'trabajadores': trabajadores})


if __name__ == '__main__':
    app.run(debug=True, port=4000)
