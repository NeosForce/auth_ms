from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from authApp.serializers.userSerializer import UserSerializer

class UserCreateView(views.APIView):

    def post(self, request, *args, **kwargs):
        #En esta parte la peticion es leida
        #En request se obtiene la peticion ( request - request header - body)
        #El request.data se recibe como json
        serializer = UserSerializer(data=request.data) # Crea un serializador
        serializer.is_valid(raise_exception=True) #Si no es valido el usuario lance un error
        serializer.save() # guardar el usuario en la base de datos

        tokenData = {"username":request.data["username"],
                     "password":request.data["password"]}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)

        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)