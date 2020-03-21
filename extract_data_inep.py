import requests
import os
from tqdm import tqdm
from bs4 import BeautifulSoup

path_directory = "/home/matteus-paula/Downloads/"
file_name = "microdados_educacao_basica_2018.zip"

result = requests.get("http://inep.gov.br/web/guest/microdados")
src = result.content

soup = BeautifulSoup(src, 'lxml')

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