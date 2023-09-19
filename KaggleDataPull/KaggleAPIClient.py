import kaggle
import tempfile

class KaggleAPIClient():

    def __init__(self, datasetUrl:str, endpoint: str):

        self.datasetURL = datasetUrl
        self.endpoint = endpoint

    def createTemp(self):

        tmp_dir = tempfile.mkdtemp()
        self.tmp_dir = tmp_dir

    def downloadDataset(self):

        try:

            success = kaggle.api.dataset_download_file(self.datasetURL, file_name=self.endpoint, path=self.tmp_dir)

        except Exception as e:

            return {"success": False, "error_message": str(e)}
        
        return success
    

