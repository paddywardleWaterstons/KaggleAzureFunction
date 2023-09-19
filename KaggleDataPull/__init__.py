import logging
import azure.functions as func
from .DownloadKaggle import DownloadKaggle
from .KaggleAPIClient import KaggleAPIClient
from .DataProcessor import DataProcessor
from .OutputBinding import OutputBinding

def main(req: func.HttpRequest, outputBlob: func.Out[str]) -> func.HttpResponse:

    datasetURL = req.headers.get('datasetURL', 'rsrishav/youtube-trending-video-dataset')
    endpoint = req.headers.get('endpoint', 'BR_category_id.json')
    logging.info("Retrieved API Request Headers.")

    kaggleClient = KaggleAPIClient(datasetURL, endpoint)
    kaggleClient.createTemp()
    kaggleClient.downloadDataset()
    logging.info("Pulled Kaggle Data.")
    
    dataProc = DataProcessor(endpoint, kaggleClient.tmp_dir)
    kaggle_data = dataProc.process_data()
    logging.info("Processed Kaggle Data.")

    if kaggle_data['success'] == True:
        outputBinding = OutputBinding(outputBlob)
        outputBinding.saveInBlob(kaggle_data["data"], endpoint)
        return func.HttpResponse("Success", status_code=200)
    else:
        return func.HttpResponse(kaggle_data['error_message'], status_code=500)
