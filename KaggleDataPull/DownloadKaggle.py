import os
import kaggle
import csv
import json
import zipfile
import tempfile
import logging

def DownloadKaggle(datasetURL:str, endpoint:str):

    try:
        # filepath = os.path.join(local_path, endpoint)

        kaggle_success = kaggle.api.dataset_download_file(datasetURL, file_name=endpoint)

        logging.info(f"Download {kaggle_success}")

        if endpoint.endswith('.csv'):

            with zipfile.ZipFile(endpoint+".zip", 'r') as z:
                z.extractall()

            if os.path.exists(endpoint+".zip"):
                os.remove(endpoint+".zip")

            with open(endpoint, 'r', encoding='ISO-8859-1') as file:

                csv_data = csv.DictReader(file)

                data_ls = []
                
                for row in csv_data:
                    data_ls.append(row)

                data = json.dumps(data_ls, indent=4)
                data = data.replace('[', '{').replace(']', '}')

        elif endpoint.endswith('.json'):

            with open(endpoint, 'r') as file:
                
                data = json.load(file)
            
            data = json.dumps(data, indent=4)

        if os.path.exists(endpoint):
            os.remove(endpoint)

        return {"success": True, "data": data}

    except Exception as e:

        return {"success": False, "error_message": str(e)}
