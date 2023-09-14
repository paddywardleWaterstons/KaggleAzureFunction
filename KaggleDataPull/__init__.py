import logging

import azure.functions as func
import os

from .DownloadKaggle import DownloadKaggle

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # get http request parameters
    # datasetURL = req.params.get('datasetURL', 'rsrishav/youtube-trending-video-dataset')
    datasetURL = req.headers.get('datasetURL', 'rsrishav/youtube-trending-video-dataset')
    endpoint = req.headers.get('endpoint', 'BR_category_id.json')
    # endpoint = req.params.get('endpoint', 'BR_category_id.json')

    logging.info('Read URL parameters.')

    result = DownloadKaggle(datasetURL, endpoint)

    logging.info('Read Kaggle Dataset')

    if result['success'] == True:
        return func.HttpResponse(result['data'], mimetype="application/json", status_code=200)
    else:
        return func.HttpResponse(result['error_message'], status_code=500)
