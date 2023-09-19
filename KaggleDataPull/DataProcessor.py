import os
import json
import zipfile
import shutil

class DataProcessor:

    def __init__(self, endpoint: str, tmp_dir: str):

        self.endpoint = endpoint
        self.tmp_dir = tmp_dir

    def process_data(self):

        try:
            file_path = os.path.join(self.tmp_dir, self.endpoint)

            if self.endpoint.endswith('.csv'):
                data = self.process_csv(file_path)
            elif self.endpoint.endswith('.json'):
                data = self.process_json(file_path)

            shutil.rmtree(self.tmp_dir)

            return {"success": True, "data": data}

        except Exception as e:

            return {"success": False, "error_message": str(e)}

    def process_csv(self, file_path: str):

        with zipfile.ZipFile(file_path+'.zip', 'r') as z:
            z.extractall(path=self.tmp_dir)

        if os.path.exists(file_path+'.zip'):
            os.remove(file_path+".zip")

        with open(file_path, 'r', encoding='ISO-8859-1') as file:
            data = str(file.read())

        return data
    
    def process_json(self, file_path: str):

        with open(file_path, 'r') as file:
                
            data = json.load(file)
            
        data = json.dumps(data, indent=4)

        return data