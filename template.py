import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

project_name = 'cnnClassifire'

list_of_files = [
    '.github/workflows/.gitkeep',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/pipline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    "config/config.yaml",
    "dvc.yml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
    "templates/index.html"

]

for filepth in list_of_files:
    filepth = Path(filepth)
    filedir, filename = os.path.split(filepth)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'creating directory; {filedir} for the file : {filename}')

    if (not os.path.exists(filepth)) or (os.path.getsize(filepth) == 0):
        with open(filepth,"w") as f:
            pass
        logging.info(f"Creating empty file:{filepth}")

    else:
        logging.info(f"{filepth} already exists")

