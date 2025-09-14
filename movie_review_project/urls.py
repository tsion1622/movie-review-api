from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from reviews.views import ReviewViewSet, MovieViewSet
from django.contrib.auth.models import User
from rest_framework import viewsets, serializers
from reviews.views import MovieViewSet, ReviewViewSet, UserViewSet, ReviewCommentViewSet, ReviewLikeViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'reviews', ReviewViewSet, basename='review')
router.register(r'movies', MovieViewSet, basename='movies') 
router.register(r'review-comments', ReviewCommentViewSet)
router.register(r'review-likes', ReviewLikeViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
