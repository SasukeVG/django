from django.urls import path
from.views import *
from . import views


urlpatterns = [
    path('', views.PostView.as_view()),
    path('<int:pk>/',views.PostDetail.as_view()),
]