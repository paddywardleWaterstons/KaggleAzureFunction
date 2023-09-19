import kaggle
import tempfile

class KaggleAPIClient():

    def __init__(self, datasetUrl:str, endpoint: str):

        self.datasetURL = datasetUrl
        self.endpoint = endpoint
        self.tmpDir = tempfile.mkdtemp()

    def downloadDataset(self):

        try:

            success = kaggle.api.dataset_download_file(self.datasetURL, file_name=self.endpoint, path=self.tmpDir)

        except Exception as e:

            return {"success": False, "error_message": str(e)}
        
        return success
    
    def getDatasetURL(self):

        return self.datasetURL
    
    def getEndpoint(self):

        return self.endpoint
    
    def getTmpDir(self):
        
        return self.tmpDir
    

