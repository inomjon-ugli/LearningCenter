from .serializers import GroupSerializers
from .models import Group
from rest_framework import generics


class CreateGroupAPIView(generics.CreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializers

class ListGroupAPIView(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializers

class DetailGroupAPIView(generics.RetrieveAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializers

class UpdateGroupAPIView(generics.UpdateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializers

class DeleteGroupAPIView(generics.DestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializers