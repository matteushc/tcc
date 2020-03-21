import requests
import os
import re
import urllib.request as request
from tqdm import tqdm
from bs4 import BeautifulSoup

path_directory = ""
files_remuneracao = "REMUNERACAO_PROFISSIONAIS_EDUCACAO_.+\.CSV"
dados_consolidados = "DADOS_CONSOLIDADOS_2017.CSV"

result = requests.get("https://www.fnde.gov.br/index.php/fnde_sistemas/siope/relatorios/arquivos-dados-analiticos")
src = result.content

soup = BeautifulSoup(src, 'lxml')

download_content = soup.find('div',{'class':'itemFullText'})

for p in download_content.find_all('p'):
    if p.text == '2017':

        xml_uls = p.find_next_sibling('ul')
        
        for j in xml_uls.find_all('li'):
            for x in j.find_all('a'):
                url = x.attrs['href']
                download_name = os.path.basename(url)

                z = re.match(files_remuneracao, download_name)
                if z or download_name == dados_consolidados:
                    with tqdm.wrapattr(open(path_directory + download_name, "wb"),
                        "write", miniters=1, desc=download_name) as fout:
                        for chunk in request.urlopen(url):
                            fout.write(chunk)
                            