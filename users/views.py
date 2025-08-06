from rest_framework.views import APIView
from .serializers import RegisterSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import CustomUser, Profil
from .serializers import UserSerializer, ProfilSerializer
from rest_framework import generics





class RegisterAPIView(APIView):

    def post(self, request):

        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'user':serializer.data,
                'message':'User registred seccessfully'
            },status = status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserListAPIView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer



class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class ProfilUpdateAPIView(generics.UpdateAPIView):
    queryset = Profil.objects.all()
    serializer_class = ProfilSerializer
    print(serializer_class.data)