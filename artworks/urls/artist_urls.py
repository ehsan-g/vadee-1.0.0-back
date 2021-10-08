from django.urls import path
from artworks.views import artist_views as views


urlpatterns = [
    path('', views.fetchArtists, name='artists'),
    path('<int:pk>/artworks/', views.fetchArtistArtworks, name='artist_artworks'),
]
