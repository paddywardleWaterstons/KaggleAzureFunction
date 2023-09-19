import azure.functions as func

class OutputBinding:

    def __init__(self, outputBlob: func.Out[str]):
        
        self.outputBlob = outputBlob

    def saveInBlob(self, data: str, endpoint: str):

        self.outputBlob.set(data)
