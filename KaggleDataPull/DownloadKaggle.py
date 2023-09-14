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

        if endpoint.endswith('.csv'):

            with zipfile.ZipFile(tmp_file_path+".zip", 'r') as z:
                z.extractall()

            # if os.path.exists(tmp_file.name+".zip"):
            #     os.remove(endpoint+".zip")

            with open(tmp_file_path, 'r', encoding='ISO-8859-1') as file:

                csv_data = csv.DictReader(file)

                data_ls = []
                
                for row in csv_data:
                    data_ls.append(row)

                data = json.dumps(data_ls, indent=4)
                data = data.replace('[', '{').replace(']', '}')

        elif endpoint.endswith('.json'):

            with open(tmp_file_path, 'r') as file:
                
                data = json.load(file)
            
            data = json.dumps(data, indent=4)

        shutil.rmtree(tmp_dir)
        
        return {"success": True, "data": data}

    except Exception as e:

        return {"success": False, "error_message": str(e)}
