from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.parsers import MultiPartParser
from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema
from . Inference import Inference
from . import ApiSerializers
import logging
logger = logging.getLogger(__name__)
from rest_framework.decorators import action

class ImagePrediction(generics.GenericAPIView):
    serializer_class = ApiSerializers.Image
    permission_classes = (AllowAny,)
    authentication_classes = []
    parser_classes = ((MultiPartParser),)

    @swagger_auto_schema(method='post',responses={200:ApiSerializers.Result})
    @action(detail=True, methods=['post'])
    def post(self, request, *args, **kwargs):
        serializer = ApiSerializers.Image(data=request.data)
        if serializer.is_valid():
            print(serializer)
            image_predictor = Inference(model_file='trained-cnn-epoch-18.pth')
            return Response(image_predictor.get_image_prediction
                            (image_bytes=serializer.validated_data.get('image').read()))
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
