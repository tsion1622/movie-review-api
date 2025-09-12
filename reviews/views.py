# reviews/views.py
from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from .models import Movie, Review, ReviewComment, ReviewLike
from .serializers import MovieSerializer, ReviewSerializer, UserSerializer, ReviewCommentSerializer, ReviewLikeSerializer
from .permissions import IsOwnerOrReadOnly
from .pagination import StandardResultsSetPagination
# -----------------------------
# Pagination
# -----------------------------
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 50


# -----------------------------
# Movie ViewSet
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().order_by("-created_at")
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title", "description"]
    ordering_fields = ["created_at", "title"]

    @action(detail=True, methods=["get"], url_path="reviews")
    def reviews(self, request, pk=None):
        """
        Endpoint: /api/movies/<id>/reviews/
        Returns paginated reviews for a specific movie.
        Supports optional filtering by rating and search by content.
        """
        movie = get_object_or_404(Movie, pk=pk)
        queryset = Review.objects.filter(movie_title=movie.title).order_by("-created_at")

        # Filter by rating (optional)
        ratings = request.query_params.get("rating")
        if ratings:
            rating_list = [int(r) for r in ratings.split(",") if r.isdigit()]
            queryset = queryset.filter(rating__in=rating_list)

        # Search by content (optional)
        search = request.query_params.get("search")
        if search:
            queryset = queryset.filter(content__icontains=search)

        # Paginate the queryset
        paginator = StandardResultsSetPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = ReviewSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

# -----------------------------
# Review ViewSet
# -----------------------------
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all().order_by("-created_at")
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ["content", "movie_title"]  # fixed to match your model
    filterset_fields = ["rating"]
    ordering_fields = ["rating", "created_at"]
    ordering = ["-created_at"]

    def perform_create(self, serializer):
        # Automatically attach logged-in user
        serializer.save(user=self.request.user)


# -----------------------------
# User ViewSet
# -----------------------------
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# -----------------------------
# ReviewComment ViewSet
# -----------------------------
class ReviewCommentViewSet(viewsets.ModelViewSet):
    queryset = ReviewComment.objects.all().order_by("created_at")
    serializer_class = ReviewCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    pagination_class = StandardResultsSetPagination

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# -----------------------------
# ReviewLike ViewSet
# -----------------------------
class ReviewLikeViewSet(viewsets.ModelViewSet):
    queryset = ReviewLike.objects.all().order_by("-created_at")
    serializer_class = ReviewLikeSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
