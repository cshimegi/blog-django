from django.db import models

from users.models import User


class Post(models.Model):
    title = models.CharField(max_length=64, null=False, blank=False)
    content = models.TextField()
    user = models.ForeignKey(User, to_field='id', related_name='user_id', on_delete=models.CASCADE)
