from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def calculator(request):
    # 입력 받을 변수
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    operators = request.GET.get('operators')

    #계산
    if operators == '+' :
        result = int(num1) + int(num2)
    elif operators =='-':
        result = int(num1) - int(num2)
    elif operators =='*':
        result = int(num1) * int(num2)
    elif operators =='/':
        result = int(num1) / int(num2)
    else:
        result = 0

    # return HttpResponse('계산기 기능 구현 시작')
    return render(request, 'calculator.html', {'result': result})