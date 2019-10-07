from flask_restful import reqparse, Resource
from loadModel import LoadModel

parser = reqparse.RequestParser()
parser.add_argument('EP', type=int, help="EP es requerido y debe ser int")
parser.add_argument('DT', type=int, help="DT es requerido y debe ser int")
parser.add_argument('DD', type=int, help="DD es requerido y debe ser int")
parser.add_argument('PC', type=int, help="PC es requerido y debe ser int")
parser.add_argument('UR', type=int, help="UR es requerido y debe ser int")
parser.add_argument('E', type=int, help="E es requerido y debe ser int")
parser.add_argument('SM', type=int, help="SM es requerido y debe ser int")

model = None

class Predecir(Resource):
    def post(self, model_type):
        args = parser.parse_args()
        global model
        if not model or model.model_type != model_type:
            model = LoadModel(model_type)

        to_predict = [(args["EP"], args["DT"], args["DD"], args["PC"], args["UR"], args["E"], args["SM"])]
        prediction = model.predict(to_predict)
        return {"satisfaccion_servicio" : prediction[0]}
