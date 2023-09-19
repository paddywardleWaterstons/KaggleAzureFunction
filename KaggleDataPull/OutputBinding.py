import os
import azure.functions as func
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

class OutputBinding:

    def __init__(self, containerName: str):
        
        self.containerName = containerName
        self.connectionString = os.environ["AzureWebJobsStorage"]
        
    def createContainerClient(self):

        blobServiceClient = BlobServiceClient.from_connection_string(self.connectionString)

        containerClient = blobServiceClient.get_container_client(container=self.containerName)

        return containerClient
    
    def saveInBlob(self, data: str, endpoint: str, containerClient: ContainerClient):

        blobClient = containerClient.get_blob_client(endpoint)

        blobClient.upload_blob(data)

    def getContainerName(self):

        return self.containerName
    
    def getConnectionString(self):

        return self.connectionString


    

