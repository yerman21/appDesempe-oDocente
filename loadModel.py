from pyspark import SparkContext
from pyspark.sql import SQLContext, SparkSession
from pyspark.ml import PipelineModel
#from pyspark.mllib.util import MLUtils

class LoadModel(object):
    _spark = None

    def __init__(self, pathModel):
        self.model = None        
        self.features = ["Experiencia Profesional", "Dominio de Temas", "Didactica del Docente", 
        "Planificacion de Clases", "Uso de Recursos", "Evaluacion", "Servicio Misionero"]
        self.model = PipelineModel.load(pathModel)
        _spark = SparkSession.builder.appName("Desempenho_Docente").getOrCreate()
        SparkContext.getOrCreate()
    
    def predict(self, listTuplesToPredict):
        if not self.model:
            return
        df_to_predict = _spark.createDataFrame(listTuplesToPredict, self.features)
        prediction = self.model.transform(df_to_predict)
        prediction.select('prediction','probability').show()
        return prediction.select("prediction","probability")