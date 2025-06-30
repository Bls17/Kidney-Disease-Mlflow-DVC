import os
from pathlib import Path
import logging

logging_str = "[%(asctime)s]: %(message)s:"

logging.basicConfig(level=logging.INFO, format=logging_str)

project_name = "cnnClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/constant/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/commons.py",
    "config/config.yaml",
    "params.yaml",
    "dvc.yaml",
    "main.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
    "README.md",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    file_dir, filename = os.path.split(filepath)

    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"directory {file_dir} created for {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            logging.info(f"creating file {filename}")

    else:
        logging.info("file already created")
