from django.shortcuts import render, get_object_or_404
from .models import Train, Station, Passenger
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect

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

            # 获取之前存储在 Session 中的已选择乘客信息
            selected_passengers = request.session.get('selected_passengers', [])
            selected_passengers.append(passenger.id)

            # 更新 Session 中的已选择乘客信息
            request.session['selected_passengers'] = selected_passengers

            # 更新相关信息
            train.ticketNum -= 1
            train.save()

            # 最后重定向到某个页面或返回适当的响应
            return HttpResponseRedirect(request.path_info)

    # 其他渲染页面的逻辑
    non_passengers = Passenger.objects.exclude(trains=train)

    # 获取 Session 中的已选择乘客信息并传递给模板
    selected_passenger_ids = request.session.get('selected_passengers', [])
    selected_passengers = Passenger.objects.filter(id__in=selected_passenger_ids)

    return render(request, 'trains/train.html', {'train': train, 'non_passengers': non_passengers, 'selected_passengers': selected_passengers})