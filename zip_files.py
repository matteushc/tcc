import zipfile
import glob
import shutil
import os

path_directory = "/home/matteus-paula/Downloads/"
target_directory = f"{path_directory}dados_inep/"
zip_name = "microdados_educacao_basica_2018.zip"
file_to_work = "ESCOLAS.zip"

def filebrowser(word=""):
    """Returns a list with all files with the word/extension in it"""
    file = []
    for f in glob.glob(f"{target_directory}microdados_ed_basica_2018/**/*", recursive=True):
        if word in f:
            file.append(f)
            return file

def extract_zip(file_name, target_directory):
    with zipfile.ZipFile(file_name, 'r') as zip_ref:
        zip_ref.extractall(target_directory)

extract_zip(f"{path_directory}microdados_educacao_basica_2018.zip", target_directory)

extract_file = filebrowser(file_to_work)

extract_file = "".join(extract_file)

extract_zip(extract_file, target_directory)

directory = [target_directory + d for d in os.listdir(target_directory) if os.path.isdir(target_directory + d)]
shutil.rmtree("".join(directory))





