import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%asctime)s] %(levelname)s: %(message)s')

project_name = "MLProject"
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
     f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
     f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "configs/config.yaml",
    "params.yaml",
    "app.py","schema.yaml","main.py","apps.py","Dockerfile","requirements.txt","setup.py",
    "research/README.md",
    "research/trails.ipynb","templates/index.html"]
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    try:
        if filedir != "":
            os.makedirs(filedir, exist_ok=True)
            logging.info(f"Created directory: {filedir} for file: {filename}")
        if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
            with open(filepath, "w") as f:
                pass
            logging.info(f"Created empty file: {filepath}")
        else:
            logging.info(f"File already exists and is not empty: {filepath}")
    except Exception as e:
        logging.error(f"Error creating file {filepath}: {e}")
