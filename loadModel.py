import pickle

class LoadModel(object):
    _directory = "model_prediction"
    models = ("naivebayes", "multinomial")
    models_path = ("gaus_model_desempeñoD_pickle", "model_desempeñoD_pickle")

    def __init__(self, model_type):
        import os.path
        try :
            index_model_path = LoadModel.models.index(model_type)
        except ValueError as e:
            print("El tipo de modelo {} no se encuentra".format(model_type))
            return None

        path_model = os.path.join(self._directory, LoadModel.models_path[index_model_path])
        if not os.path.isfile(path_model):
            print("No se encontro el modelo {} para cargar".format(path_model))
            return None
                    
        self.model_type = model_type
        self.model = pickle.load(open(path_model, 'rb'))
        print("Modelo cargado")

    def predict(self, listTuplesToPredict):
        if not self.model:
            return None
        return self.model.predict(listTuplesToPredict)