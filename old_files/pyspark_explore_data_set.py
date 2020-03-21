from pyspark import SparkContext, SparkConf

df = spark.read.load("/home/matteus-paula/Downloads/dados_inep/ESCOLAS.CSV",
                     format="csv", sep="|", inferSchema="true", header="true")

df.select(["NO_ENTIDADE","CO_MUNICIPIO"]) \
    .where("CO_UF = 31 and IN_INTERNET = 0 and CO_MUNICIPIO = 3131703") \
    .show(100,truncate=False)
