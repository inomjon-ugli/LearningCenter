from django.urls import path
from .views import CreateCourseAPIView,ListCourseAPIView,DetailCourseAPIView,UpdateCourseAPIView,DeleteCourseAPIView


urlpatterns = [
    path('create/',CreateCourseAPIView.as_view()),
    path('list/',ListCourseAPIView.as_view()),
    path('detail/<int:pk>/',DetailCourseAPIView.as_view()),
    path('update/<int:pk>/',UpdateCourseAPIView.as_view()),
    path('delete/<int:pk>/',DeleteCourseAPIView.as_view()),
]