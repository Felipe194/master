#Integrantes GRUPO 3-B
# • Felipe Rodríguez
# • Cesar Triviño
# • Nelson Acurio
# • Richard Ramos

import string
from flask import Flask, jsonify, request,render_template,url_for
from productos import productos
app = Flask(__name__,template_folder='Template')
#from jinja2 import Markup


@app.route('/')
def hola():
    return render_template("Productos.html")

@app.route('/lista')
def lista():
    return jsonify({"message": "productos"})

@app.route('/productos', methods=['GET'])
def getProdu():
    return jsonify(productos)
@app.route('/get_Productos', methods=['GET','POST'])
def get_productos():
    if request.method=='POST':
        elemento=request.form.get("elemento")
        listpro = [produc for produc in productos if produc['name'] == elemento.lower()]
        print(listpro)
        if (len(listpro) > 0):
            lista=jsonify({"productos": listpro[0]})
            #return render_template("Productos.html",lista=lista)
            return jsonify({"productos": listpro[0]})
        #return listpro
    return "No existe ese producto"
        

@app.route('/productos/<string:produc_name>', methods=['GET'])
def getProduc(produc_name):
    listpro = [produc for produc in productos if produc['name'] == produc_name.lower()]
    if (len(listpro) > 0):
        return render_template(jsonify({"productos": listpro[0]}))
    return jsonify({"message": "producto no encontrado"})

@app.route('/productos', methods=['POST'])
def addProduc():
    #print(request.json)
    new_produc = {
        "name": request.json['name'],
        "precio": request.json['precio'],
        "cantidad": request.json['cantidad']
    }
    productos.append(new_produc)
    #return 'recibido'
    return jsonify({"message": "producto agregado", 'productos': productos})
#actualizar dato

@app.route('/productos/<string:produc_name>', methods=['PUT'])
def editproduc(produc_name):
    actual = [produc for produc in productos if produc['name'] == produc_name]
    if (len(actual) > 0):
        actual[0]['name'] = request.json['name'],
        actual[0]['precio'] = request.json['precio'],
        actual[0]['cantidad'] = request.json['cantidad']
        return jsonify({
            "message": "producto actualizado",
            "productos": actual[0]
        })
    return jsonify({"message": "producto no encontrado"})
#metodo delete

@app.route('/productos/<string:produc_name>', methods=['DELETE'])
def deleteproduc(produc_name):
    eliminarproduc = [produc for produc in productos if produc['name'] == produc_name]
    if len(eliminarproduc) > 0:
        productos.remove(eliminarproduc[0])
        return jsonify({
            'message': 'Producto eliminado',
            'products': productos
        })
    return jsonify({"message": "no encontrado"})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)