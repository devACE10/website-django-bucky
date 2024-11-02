from django.urls import path, re_path
from music import views

app_name = 'music'

urlpatterns = [
    # /music/
    path('', views.IndexView.as_view(), name='index'),

    path('register/', views.UserFormView.as_view(), name='register'),

    # /music/<album_id>/
    re_path(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /music/album/add/
    path('album/add/', views.AlbumCreate.as_view(), name='album-add'),

    # /music/album/<pk>/
    re_path(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),

    # /music/album/<pk>/delete
    re_path(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),
]
