from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    movie_title = models.CharField(max_length=200)
    review_text = models.TextField()
    rating = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.movie_title} - {self.user.username}"