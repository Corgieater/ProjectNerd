from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
import datetime

class List(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    describe = models.TextField(blank=True)
#
#     def has_delete_authority(self, user_id):
#         if self.owner == user_id:
#             return True
#
#


class UserListRelation(models.Model):
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    list_id = models.ForeignKey(List, on_delete=models.CASCADE)


class Song(models.Model):
    title = models.CharField(max_length=200)
    review = models.TextField(blank=True)
    modified_date = models.DateField(default=datetime.date.today)
    author = models.CharField(max_length=200)
    url = models.CharField(max_length=150)
    tag_relation_id = models.IntegerField(null=True)


class ListSongRelation(models.Model):
    list_id = models.ForeignKey(List, on_delete=models.CASCADE)
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)


class Tag(models.Model):
    name = models.CharField(max_length=50)
    total_reference = models.IntegerField(default=1)
    created_time = models.DateField(default=datetime.date.today)
