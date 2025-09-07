from rest_framework import viewsets, permissions
from .models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer
from .permissions import IsOwnerOrReadOnly


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ReviewViewSet(viewsets.ModelViewSet):
    ...
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['comment', 'movie__title']   # for search
    filterset_fields = ['rating']                 # for filtering
    ordering_fields = ['rating', 'created_at']    # for sorting
    ordering = ['-created_at']                    # default order