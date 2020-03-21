import requests
import os
import re
import shutil
import urllib.request as request
from contextlib import closing
from tqdm import tqdm
from bs4 import BeautifulSoup


path_directory = ""
file_name = "REMUNERACAO_PROFISSIONAIS_EDUCACAO_.+\.CSV"

result = requests.get("https://www.fnde.gov.br/index.php/fnde_sistemas/siope/relatorios/arquivos-dados-analiticos")
src = result.content

soup = BeautifulSoup(src, 'lxml')

download_content = soup.find('div',{'class':'itemFullText'})

for p in download_content.find_all('p'):
    if p.text == '2017':

        xml_uls = p.find_next_sibling('ul')
        
        for j in xml_uls.find_all('li'):
            url = j.find('a').attrs['href']
            download_name = os.path.basename(url)
            
            z = re.match(file_name, download_name)
            if z:
                with closing(request.urlopen(url)) as r:
                    with open(path_directory + download_name, 'wb') as f:
                        shutil.copyfileobj(r, f)