from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def calculator(request):
    # return HttpResponse('계산기 기능 구현 시작')
    # render => 템플릿 가져오기 = html
    # 1. 데이터 확인
    num1 = int(request.GET.get('num1'))
    num2 = int(request.GET.get('num2'))
    operators = request.GET.get('operators')

    # 2. 연산
    if operators == '+':
        result = num1 + num2
    elif operators == '-':
        result = num1 - num2
    elif operators == '*':
        result = num1 * num2
    elif operators == '/':
        result = num1 / num2
    else:
        result = 0

    # 3. 응답
    return render(request, 'calculator.html', {'result': result})

# 로또 번호 추출기


def lotto(request):
    import random
    lotto_number = list()
    for _ in range(7):
        number = random.randint(1, 45)
        lotto_number.append(number)

    return render(request, 'lotto.html', {'lotto_number': lotto_number})
