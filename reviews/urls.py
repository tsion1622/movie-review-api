from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'movies', MovieViewSet, basename='movies')

urlpatterns = [
    path('', include(router.urls)),
    path('movies/<int:movie_pk>/reviews/', ReviewViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
]
