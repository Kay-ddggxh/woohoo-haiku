from . import views
from django.urls import path


urlpatterns = [
    path('', views.HaikuList.as_view(), name='home'),
    path('like/<slug:slug>', views.HaikuLike.as_view(), name='haiku_like'),
    path('create_haiku/', views.CreateHaiku.as_view(), name='create_haiku'),
    path('<slug:slug>/', views.HaikuDetail.as_view(), name='haiku_detail'),
    path('update/<int:pk>', views.UpdateHaiku.as_view(), name='update'),
]
