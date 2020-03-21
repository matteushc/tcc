from pyspark.sql.functions import *

diretorio = "/home/matteus-paula/Downloads/dados_tcc/remun_docentes"

df = spark.read.option("encoding", "ISO-8859-1").csv(f'{diretorio}/*.CSV', header=True, sep=';')

df_2 = df.select(['CO_MUNICIPIO','NO_PROFISSIONAL', 'CO_UF', 'VL_TOTAL', 'CATEG_PROFISSIONAL', 'TP_CATEGORIA'])


list_categ = ['Docente habilitado em curso de pedagogia', 
'Docente habilitado em curso de licenciatura plena', 
'Docente habilitado em curso de nível médio',
'Profissionais em efetivo exercício no âmbito da educação infantil e ensino fundamental.']

df_3 = df_2.filter((col('CATEG_PROFISSIONAL').isin(list_categ)) & (col('TP_CATEGORIA') == lit('PROFISSIONAIS DO MAGISTÉRIO')))

df_4 = df_3.select(['CO_MUNICIPIO','NO_PROFISSIONAL', 'CO_UF', 'VL_TOTAL'])

df_4 = df_4.withColumn('VL_TOTAL', regexp_replace('VL_TOTAL',',','.').cast('float'))

df_5 = df_4.groupBy(['CO_MUNICIPIO','NO_PROFISSIONAL', 'CO_UF']).agg(round(mean("VL_TOTAL"), 2))

df_6 = df_5.withColumnRenamed('round(avg(VL_TOTAL), 2)', 'VL_TOTAL')

df_6.coalesce(1).write.csv(f'{diretorio}/remuneracao_media_docentes.csv', sep=';', header='true')