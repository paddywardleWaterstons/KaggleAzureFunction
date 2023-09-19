import os
import json
import zipfile
import shutil

class DataProcessor:

    def __init__(self, endpoint: str, tmpDir: str):

        self.endpoint = endpoint
        self.tmpDir = tmpDir

    def processData(self):

        try:
            file_path = os.path.join(self.tmpDir, self.endpoint)

            if self.endpoint.endswith('.csv'):
                data = self.processCsv(file_path)
            elif self.endpoint.endswith('.json'):
                data = self.processJson(file_path)

            shutil.rmtree(self.tmpDir)

            return {"success": True, "data": data}

        except Exception as e:

            return {"success": False, "error_message": str(e)}

    def processCsv(self, file_path: str):

        with zipfile.ZipFile(file_path+'.zip', 'r') as z:
            z.extractall(path=self.tmpDir)

        if os.path.exists(file_path+'.zip'):
            os.remove(file_path+".zip")

        with open(file_path, 'r', encoding='ISO-8859-1') as file:
            data = str(file.read())

        return data
    
    def processJson(self, file_path: str):

        with open(file_path, 'r') as file:
                
            data = json.load(file)
            
        data = json.dumps(data, indent=4)

        return data
    
    def getEndpoint(self):

        return self.endpoint
    
    def getTmpDir(self):

        return self.tmpDir
    