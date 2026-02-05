import logging
from datetime import datetime
import sys
import os
from pathlib import Path
#Start Logging
#By using Logging we can track the program events and errors format control style and using level we
#control secuirity
log_file="project.log"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename=log_file
)
project_name="Hate"
list_of_files=[
    #Components Package
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",

    #Configuration
    f"{project_name}/Configuration/gcloud_syncer.py",
    
    #Constant
    f"{project_name}/Constant/__init__.py",
    
    #Entity
    f"{project_name}/Entity/__init__.py",
    f"{project_name}/Entity/Config_entity.py",
    f"{project_name}/Entity/Artifact_entity.py",

    #Exception
    f"{project_name}/Exception/__init__.py",
    
    #Logger
    f"{project_name}/Logger/__init__.py",
    
    #Pipeline
    f"{project_name}/Pipeline/__init__.py",
    f"{project_name}/Pipeline/train_pipeline.py",
    f"{project_name}/Pipeline/prediction_pipeline.py",
    
    #ML
    f"{project_name}/Ml/__init__.py",
    f"{project_name}/Ml/model.py",

    "app.py",
    "demo.py",
    "requirements.txt",
    "DockerFile",
    "setup.py",
    ".dockerignore"
]

for filepath in list_of_files:
    filepath=Path(filepath)
    folder,filename=os.path.split(filepath)
#when we split a file from its path in return we have two things filename 
#and the folder name 
 # Folder create karo agar name diya gaya ho
    if folder != "":
        os.makedirs(folder, exist_ok=True)
        logging.info(f"Creating Directory : {folder} for the {filename}")

# File create karo agar exist nahi karti ya empty hai
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
          pass
        logging.info(f"Creating Empty File : {filepath}")

    else:
        logging.info(f"{filename} already exists")

