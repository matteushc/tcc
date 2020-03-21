import requests
import os
from tqdm import tqdm
from bs4 import BeautifulSoup

path_directory = "/path/"

def extractInepMicroDados():
	file_name = "micro_censo_escolar_2017.zip"

	result = requests.get("http://inep.gov.br/web/guest/microdados")
	src = result.content

	soup = BeautifulSoup(src, 'html.parser')

	censo_escolar = soup.find('div',{'data-anchor':'censo-escolar'})

	download_content = censo_escolar.find('div',{'class':'list-download__content'})

	for x in download_content.find('ul').find_all('a'):
		url = x.attrs['href']

		download_name = os.path.basename(url)
		if file_name == download_name:
			
			r = requests.get(url, stream=True)
			total_size = int(r.headers.get('content-length', 0))
			block_size = 1048576
			t=tqdm(total=total_size)
			with open(path_directory + download_name, 'wb') as fobj:
				for data in r.iter_content(block_size):
					t.update(len(data))
					fobj.write(data)
			t.close()
			
def extractIDEBResultadosEscolas():
	file_name_anos_iniciais = "divulgacao_anos_iniciais_municipios2017-atualizado-Jun_2019.zip"
	file_name_anos_finais = "divulgacao_anos_finais_municipios2017-atualizado-Jun_2019.zip"
	file_name_ensino_medio = "divulgacao_ensino_medio_municipios2017-atualizado-Jun_2019.zip"

	result = requests.get("http://portal.inep.gov.br/web/guest/educacao-basica/ideb/resultados")
	src = result.content

	soup = BeautifulSoup(src, 'html.parser')

	resultado_escolar = soup.find('div',{'id':'p_p_id_56_INSTANCE_6G5n5Ax2xN2I_'})
	for ul_content in resultado_escolar.find_all('ul'):
		for x in ul_content.find_all('a'):
			url = x.attrs['href']

			download_name = os.path.basename(url)
			if download_name == file_name_anos_iniciais \
				or download_name == file_name_anos_finais \
					or download_name == file_name_ensino_medio:
				
				r = requests.get(url, stream=True)
				total_size = int(r.headers.get('content-length', 0))
				block_size = 1048576
				t=tqdm(total=total_size)
				with open(path_directory + download_name, 'wb') as fobj:
					for data in r.iter_content(block_size):
						t.update(len(data))
						fobj.write(data)
				t.close()


extractInepMicroDados()
extractIDEBResultadosEscolas()