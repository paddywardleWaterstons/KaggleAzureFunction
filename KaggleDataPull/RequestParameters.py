import azure.functions as func

class RequestParameters:

    def __init__(self, req: func.HttpRequest):
        self.datasetURL = req.headers.get('datasetURL', 'rsrishav/youtube-trending-video-dataset')
        self.containerName = req.headers.get('container', 'youtube')
        self.endpoint = req.headers.get('endpoint', 'BR_category_id.json')

    def getDatasetURL(self):

        return self.datasetURL
    
    def getContainerName(self):

        return self.containerName
    
    def getEndpoint(self):

        return self.endpoint