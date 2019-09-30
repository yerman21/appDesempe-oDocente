#autor:yerry aguirre
from flask import (
	Flask,
	render_template,
	request,
    redirect,
    url_for,
    json
	)
from flask_restful import Resource, Api
from loadModel import LoadModel

#create the application instance
app = Flask(__name__, template_folder="templates")
api = Api(app)

@app.route("/", methods=["GET"])
def showData():
    model = LoadModel("myNaiveBayesModel")
    to_predict = [
        (1, 1, 1, 2, 1, 2, 2),
        (2, 1, 3, 2, 1, 1, 1),
        (1, 3, 2, 2, 1, 1, 3)
        ]
    #model.predict(to_predict)
    return "<h1>Hola boby</h1>"

def msgRequired(parametro):
    return "'"+parametro+"' son(es) requerido(s) por el sistema"

# Si estamos ejecutando en modo independiente, ejecute la aplicación
if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True, port=8000)