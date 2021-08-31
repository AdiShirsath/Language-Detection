import uvicorn

from generated.detection_pb2 import GetPredictionResponse
from make_prediction import Predictor
from generated.detection_twirp import LanguageDetectionServer
from vtwirp.asgi import TwirpASGIApp

class LanguageDetection(object):

    def GetPrediction(self, ctx, request):
        # get text
        text = request.Text
        predictor = Predictor()
        # making prediction
        prediction= predictor.make_prediction(text=text)
        # create and return response prediction
        response = GetPredictionResponse()
        response.Response = f"Predicted Language of Text is: {prediction}"
        return response


service = LanguageDetectionServer(service=LanguageDetection())
app = TwirpASGIApp()
app.add_service(service)


if __name__ == "__main__":
    uvicorn.run("server:app", host='0.0.0.0', port=3000, log_level='info')