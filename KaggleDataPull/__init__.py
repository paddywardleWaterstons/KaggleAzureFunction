import logging
import azure.functions as func
from .RequestParameters import RequestParameters
from .KaggleAPIClient import KaggleAPIClient
from .DataProcessor import DataProcessor
from .OutputBinding import OutputBinding

def main(req: func.HttpRequest) -> func.HttpResponse:

    httpParams = RequestParameters(req)
    datasetURL = httpParams.getDatasetURL()
    containerName = httpParams.getContainerName()
    endpoint = httpParams.getEndpoint()
    logging.info("Retrieved API Request Headers.")

    kaggleClient = KaggleAPIClient(datasetURL, endpoint)
    kaggleClient.downloadDataset()
    logging.info("Pulled Kaggle Data.")
    
    dataProc = DataProcessor(endpoint, kaggleClient.getTmpDir())
    kaggle_data = dataProc.processData()
    logging.info("Processed Kaggle Data.")

    if kaggle_data['success'] == True:
        outputBinding = OutputBinding(containerName)
        containerClient = outputBinding.createContainerClient()
        outputBinding.saveInBlob(kaggle_data["data"], endpoint, containerClient)
        return func.HttpResponse("Success", status_code=200)
    else:
        return func.HttpResponse(kaggle_data['error_message'], status_code=500)
