import os
import kaggle
import csv
import json
import zipfile
import tempfile
import logging
import shutil

def DownloadKaggle(datasetURL:str, endpoint:str):

    try:

        tmp_dir = tempfile.mkdtemp()
        tmp_file_path = os.path.join(tmp_dir, endpoint)
        kaggle.api.dataset_download_file(datasetURL, file_name=endpoint, path=tmp_dir)

        logging.info("Downloaded for kaggle API")
        
        if endpoint.endswith('.csv'):

            with zipfile.ZipFile(tmp_file_path+".zip", 'r') as z:
                z.extractall(path=tmp_dir)

            logging.info("Extracting Zip")

            if os.path.exists(tmp_file_path+".zip"):
                os.remove(tmp_file_path+".zip")

            logging.info("Removed zip")

            with open(tmp_file_path, 'r', encoding='ISO-8859-1') as file:

                data = str(file.read())#str(csv.DictReader(file))
            logging.info("read into csv_data")

        elif endpoint.endswith('.json'):

            with open(tmp_file_path, 'r') as file:
                
                data = json.load(file)
            
            data = json.dumps(data, indent=4)

        shutil.rmtree(tmp_dir)

        return {"success": True, "data": data}

    except Exception as e:

        return {"success": False, "error_message": str(e)}