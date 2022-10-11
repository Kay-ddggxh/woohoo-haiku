from . import views
from django.urls import path


urlpatterns = [
    path('', views.HaikuList.as_view(), name='home')
]