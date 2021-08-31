
from generated.detection_twirp import LanguageDetectionClient
import generated.detection_pb2 as pb2
from vtwirp.exceptions import TwirpServerException
from twirp.context import Context

client = LanguageDetectionClient("http://localhost:3000")
ctx=Context()

# Text languages
# Kannada - ನನ್ನ ಹೆಸರು ಆದಿತ್ಯ
# marathi - मला खात्री आहे
# Japanese - 日本の大気汚染の歴史

request = pb2.GetPredictionRequest(Text="मला खात्री आहे")

try:
     prediction = client.GetPrediction(ctx=ctx, request=request)
     print(prediction)
except TwirpServerException as e:
     print(e, e.to_dict())