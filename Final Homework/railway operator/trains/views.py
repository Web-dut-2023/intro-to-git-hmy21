

from django.shortcuts import render, get_object_or_404
import subprocess

from .models import Train, Station, Passenger, Passenger_trains
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'trains/home.html')

def index(request):
    return render(request, "trains/index.html", {
        "trains": Train.objects.all()
    })

def train(request, train_id):
    train = Train.objects.get(id=train_id)
    passengers = train.passengers.all()
    non_passengers = Passenger.objects.exclude(trains=train).all()
    return render(request, "trains/train.html", {
        "train": train,
        "passengers": passengers,
        "non_passengers": non_passengers
    })
def book(request, train_id):
    train = get_object_or_404(Train, pk=train_id)

    if request.method == 'POST':
        # 在处理表单之前检查票数是否足够
        if train.ticketNum > 0:
            passenger_id = request.POST.get('passenger')
            passenger = get_object_or_404(Passenger, pk=passenger_id)
            booking = Passenger_trains.objects.create(passenger=passenger, train=train)
            # 添加预订
            passenger.trains.add(train)

            # 更新相关信息
            train.ticketNum -= 1
            train.save()

            # 最后重定向到某个页面或返回适当的响应
            return HttpResponseRedirect(request.path_info)

    # 其他渲染页面的逻辑
    non_passengers = Passenger.objects.exclude(trains=train)

    # 获取已预订的乘客并传递给模板
    selected_passengers = Passenger.objects.filter(trains=train)

    return render(request, 'trains/train.html', {'train': train, 'non_passengers': non_passengers, 'selected_passengers': selected_passengers})
def run_python_script(request):
    script_path = 'ai.py'

    # 使用 subprocess.Popen 运行 Python 脚本，并等待脚本执行完毕
    process = subprocess.Popen(['python', script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    if process.returncode == 0:
        return HttpResponse(f"Python 脚本执行成功！\nOutput:\n{output.decode('utf-8')}")
    else:
        return HttpResponse(f"Python 脚本执行失败：\nError:\n{error.decode('utf-8')}")
"""
def chat_view(request):
    if request.method == 'POST':
        input_text = request.POST.get('input_text', '')
        chat_bot = Chat_bot('text-davinci-003')
        response_text = chat_bot.Generate()
        return JsonResponse({'response': response_text})

    return render(request, 'trains/ai.html')


def send_input(request):
    if request.method == 'POST':
        input_text = request.POST.get('input_text', '')

        # Initialize the Chat_bot and get the response
        chat_bot = Chat_bot('text-davinci-003')
        response_text = chat_bot.Generate()

        # Return the response as JSON
        return JsonResponse({'response': response_text})
    else:
        # Return an error for non-POST requests
        return JsonResponse({'error': 'Invalid method'})
        """