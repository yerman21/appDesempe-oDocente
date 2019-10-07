#autor:yerry aguirre
from flask import (
	Flask,
    request
	)
from flask_restful import Api
from loadModel import LoadModel
from web_service.Predecir import Predecir

#create the application instance
app = Flask(__name__, template_folder="templates")
api = Api(app)

model = None

api.add_resource(Predecir, '/<string:model_type>')

@app.route("/", methods=["GET"])
def index():
    return "<h1>Hola boby</h1>"

@app.route("/jojo/<string:model_type>", methods=["POST"])
def prediction(model_type):
    if not model_type:
        print("Especifique el tipo del modelo")
        return None
    
    ep = request.form["EP"]
    dt = request.form["DT"]
    dd = request.form["DD"]
    pc = request.form["PC"]
    ur = request.form["UR"]
    e = request.form["E"]
    sm = request.form["SM"]

    if not ep or not dt or not dd or not pc or not ur or not e or not sm:
        return msgRequired("ep, dt, dd, pc, ur, e y sm")
        
    global model
    if not model or model.model_type != model_type:        
        model = LoadModel(model_type)
    
    to_predict = [(int(ep), int(dt), int(dd), int(pc), int(ur), int(e), int(sm))]
#    to_predict = [
#        (1, 1, 1, 2, 1, 2, 2),
#        (2, 1, 3, 2, 1, 1, 1),
#        (1, 1, 1, 1, 1, 1, 1)
#        ]

    prediction = model.predict(to_predict)
    return "<h2>Calidad del servicio: {}</h2>".format(prediction)

def msgRequired(parametro):
    return "'"+parametro+"' son(es) requerido(s) por el sistema"

# Si estamos ejecutando en modo independiente, ejecute la aplicación
if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True, port=8000)