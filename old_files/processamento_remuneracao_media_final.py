from pyspark.sql.functions import *
from pyspark.sql import Window

diretorio = '/home/matteus-paula/Downloads/dados_tcc/dados_tratados_remun'

df = spark.read.csv(f'{diretorio}/*.csv', header=True, sep=';')

grp_window = Window.partitionBy(['CO_MUNICIPIO', 'CO_UF'])
percentile_approx = expr('percentile_approx(VL_TOTAL, 0.5)')

df_final = df.select(['CO_MUNICIPIO','CO_UF','VL_TOTAL']) \
    .groupBy(['CO_MUNICIPIO', 'CO_UF']).agg(percentile_approx.alias('VL_TOTAL'))

df_final.coalesce(1).write.csv(f'{diretorio}/remuneracao_media_docentes_final.csv', sep=';', header='true')