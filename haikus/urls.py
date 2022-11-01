from . import views
from django.urls import path


urlpatterns = [
    path('', views.HaikuList.as_view(), name='home'),
    path('<slug:slug>/', views.HaikuDetail.as_view(), name='haiku_detail'),
    path('like/<slug:slug>', views.HaikuLike.as_view(), name='haiku_like')
]
