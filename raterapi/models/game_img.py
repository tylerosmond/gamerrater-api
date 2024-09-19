from django.db import models
from django.contrib.auth.models import User

class GameImg(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uploaded_images')
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name='images')
    img_url = models.URLField()