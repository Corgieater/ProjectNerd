from django.shortcuts import render
import sys
from users import models
from .models import *
from django.http import HttpResponse
from allauth.account.decorators import verified_email_required
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .repository import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .serializers import *
from .service import *
# from .models import List
# from django.contrib.auth.models import User


sys.path.append("..")
list_repository = ListRepository()

def index(request):
    return render(request, 'index.html')


def news(request):
    return render(request, 'news.html')


# @login_required
# def my_lists(request, user_id):
#     user_lists = UserListRelation.objects.filter(user_id=user_id).values('list_id')
#     for each_list in user_lists:
#         print(each_list['list_id'])
#         content = List.objects.filter(id=each_list['list_id']).values()
#         print(content)
#     # lists = user_list.objects.filter(owner_id=user_id)
#     print(user_lists)
#     # user_list = user.get(id=user_id)
#     # print(user_list)
#     return render(request, 'my_lists.html', {'user_id': user_id})

@login_required
def my_lists(request):
    return render(request, 'my_lists.html')


# def get_user_lists_by_id(request):
#     user_id = request.user.id
#     lists = list_repository.get_all_list_by_user_id(user_id)
#     return lists

# for Chrome Extension adding cool stuff
class CEListViews(APIView):
    # getting user_list relations, in some point I should reuse this and mack a func to check if user == owner
    def get(self, request):
        try:
            user_id = request.user.id
            if user_id is None:
                return APIResponse(success=False, error="User not found", status=status.HTTP_404_NOT_FOUND)
            lists_ids = list_repository.get_all_list_by_user_id(user_id)
        except Exception as e:
            return APIResponse(success=False, error=f"Something went wrong in CEListViews(APIView).get, {e}",
                               status=status.HTTP_404_NOT_FOUND)
        serializer = ListSerializer(lists_ids, many=True)
        return APIResponse(data=serializer.data)

# def add_list(request, user_id, title, description):
#     new_list = List(user_id, title, description)
#     new_list.save()
#     return 'ok'

@login_required
def form(request):
    return render(request, 'form.html')


def get_exist_tag(request, keyword):
    print(keyword)
    tag = Tag.objects.filter(name__contains=keyword).values().order_by('-total_reference')[:5]
    print(tag)
    if len(tag) != 0:
        dic = {'tags': [], 'ok': True}
        for t in tag:
            print(t)
            dic['tags'].append({t['name']: t['id']})
        print(dic)
    else:
        dic = {'ok': False}

    return JsonResponse(dic)

