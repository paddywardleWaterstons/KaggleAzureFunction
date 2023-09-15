import logging
import azure.functions as func
from .DownloadKaggle import DownloadKaggle

def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python HTTP trigger function processed a request.')

    datasetURL = req.headers.get('datasetURL', 'rsrishav/youtube-trending-video-dataset')
    endpoint = req.headers.get('endpoint', 'BR_youtube_trending_data.csv')

    logging.info('Read URL parameters.')

    result = DownloadKaggle(datasetURL, endpoint)

    logging.info('Read Kaggle Dataset')

    if result['success'] == True:
        return func.HttpResponse(result['data'], mimetype="application/json", status_code=200)
    else:
        return func.HttpResponse(result['error_message'], status_code=500)
