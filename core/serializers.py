from rest_framework import serializers
from .models import List, UserListRelation


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ["id", "owner", "title", "describe"]


# I guess I will save it for co-editing
# class UserListRelationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserListRelation
#         fields = ('id', 'list_id_id', 'user_id_id')