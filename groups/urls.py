from django.urls import path
from .views import CreateGroupAPIView,ListGroupAPIView,DetailGroupAPIView,UpdateGroupAPIView,DeleteGroupAPIView

urlpatterns = [
    path('create/',CreateGroupAPIView.as_view()),
    path('list/',ListGroupAPIView.as_view()),
    path('detail/<int:pk>/',DetailGroupAPIView.as_view()),
    path('update/<int:pk>/',UpdateGroupAPIView.as_view()),
    path('delete/<int:pk>/',DeleteGroupAPIView.as_view()),
    
]