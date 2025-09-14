from django.contrib import admin
from .models import Movie, Review, ReviewComment, ReviewLike

# -----------------------------
# Movie Admin
# -----------------------------
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'release_date', 'created_at')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)

# -----------------------------
# Review Admin
# -----------------------------
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('movie_title', 'user', 'rating', 'created_at', 'updated_at')
    search_fields = ('movie_title', 'user__username', 'content')
    list_filter = ('rating', 'created_at', 'updated_at')
    ordering = ('-created_at',)

# -----------------------------
# ReviewComment Admin
# -----------------------------
@admin.register(ReviewComment)
class ReviewCommentAdmin(admin.ModelAdmin):
    list_display = ('review', 'user', 'content', 'created_at')
    search_fields = ('content', 'user__username', 'review__movie_title')
    ordering = ('-created_at',)


@admin.register(ReviewLike)
class ReviewLikeAdmin(admin.ModelAdmin):
    list_display = ('review', 'user', 'created_at')
    search_fields = ('user__username', 'review__movie_title')
    ordering = ('-created_at',)
