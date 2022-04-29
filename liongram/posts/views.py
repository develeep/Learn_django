import json
from re import template
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView
from .models import Post
# Create your views here.

# 함수 기반 view


def url_view(request):
    print('url_view')
    data = {"code": "001", 'msg': 'ok'}
    # return HttpResponse('<h1>url_view</h1>')
    return JsonResponse(data)


def url_parameter(request, username):
    print('url_parameter')
    print(f'username : {username}')
    print(request.GET)
    return HttpResponse(username)


def function_view(request):

    print(f'request.method: {request.method}')
    if request.method == 'GET':
        print(f'request.GET: {request.GET}')  # 데이터 받을떄
    elif request.method == 'POST':
        print(f'request.POST: {request.POST}')  # 데이터 추가,수정,삭제 할때

    return render(request, 'view.html')

# 클래스 기반 view


class class_view(ListView):
    model = Post
    template_name = 'cbv_view.html'
