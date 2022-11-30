from . import views
from django.urls import path


urlpatterns = [
    path('', views.HaikuList.as_view(), name='home'),
    path('like/<slug:slug>', views.HaikuLike.as_view(), name='haiku_like'),
    path('create_haiku/', views.CreateHaiku.as_view(), name='create_haiku'),
    path('user_haikus/', views.UserHaikus.as_view(), name="user_haikus"),
    path('<slug:slug>/', views.HaikuDetail.as_view(), name='haiku_detail'),
    path('update/<slug:slug>', views.UpdateHaiku.as_view(), name='update'),
    path('delete/<slug:slug>', views.DeleteHaiku.as_view(), name='delete'),
    path('tag_list/<tag>/', views.TagList.as_view(), name="tag_list"),
]
