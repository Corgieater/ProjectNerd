from django.db import models
from django.conf import settings
from django.shortcuts import get_object_or_404
from .models import *

# if I am using CE for adding cool stuff, that means I am the owner or co-editor of lists
# So I should search for list-owner or co-editor, not from relations?

class ListRepository:
    @staticmethod
    def get_all_list_by_user_id(user_id):
        user_lists = List.objects.filter(owner=user_id).values()

        print('repository work', user_lists)
        return user_lists

# save it for co-editing
# class UserListRelationRepository:
#     @staticmethod
#     def get_lists_by_user_id(user_id):
#         user_lists = UserListRelation.objects.filter(user_id=user_id).values()
#
#         print('repository work', user_lists)
#         return user_lists

