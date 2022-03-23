
from flask import Flask, jsonify, request

app = Flask(__name__)
# Importación de elementos
from marcasautos import autos
from modelo import modelos

#Mensaje
@app.route("/")
def index():
    return "CODIGO PARA PROBAR PUSH EN POSTMAN"
#muestra mensaje 
@app.route('/lista')
def lista():
    return jsonify({"message": "Marca de autos a la venta"})
#muestra la lista que contiene autos
@app.route('/AutosVenta')
def getautos():
    return jsonify({'Marcas': autos})
#muestra la lista que contiene modelos
@app.route('/Modelos')
def getmodelos():
    return jsonify({'Marcas': modelos})
#Metodo POST nos permite crear un recurso nuevo
#Metodo POST para autos
@app.route('/AutosVenta', methods=['POST'])
def addautos():
    nuevomodelo = {
       
        'id': request.json['id'],
        'modelo': request.json['modelo'],
        'Añofabricacion': request.json['Añofabricacion'],
        'kilometraje': request.json['kilometraje']
    }
    autos.append(nuevomodelo)
    return jsonify({'Marcas': autos})

#Metodo POST para modelos
@app.route('/Modelos', methods=['POST'])
def addmodelos():
    nuevamarca = {
       
        'id': request.json['id'],
        'modelo': request.json['modelo']

    }
    modelos.append(nuevamarca)
    return jsonify({'Nueva Marca': modelos})
    
if __name__ == '__main__':
    app.run(debug=True, port=3000)