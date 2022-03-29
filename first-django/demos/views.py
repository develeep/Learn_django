from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def calculator(request):
    # return HttpResponse('계산기 기능 구현 시작')
    # render => 템플릿 가져오기 = html
    return render(request, 'calculator.html')
