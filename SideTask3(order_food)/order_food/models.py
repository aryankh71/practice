from django.db import models
from django_comments.moderation import CommentModerator, moderator
from django_comments.abstracts import CommentAbstractModel


class Food(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=400)
    price = models.IntegerField()
    is_available = models.BooleanField(null=True)


class FoodModerator(CommentModerator):
    is_public = False
    email_notification = True
    enable_field = 'enable_comments'

moderator.register(Food, FoodModerator)


class CommentWithTitle(CommentAbstractModel):
    title = models.CharField(max_length=300)