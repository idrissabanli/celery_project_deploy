from django.shortcuts import render, HttpResponse
from .tasks import email
from django_celery_beat.models import PeriodicTask, ClockedSchedule
from django.views.generic import FormView
from .forms import ProductForm
from django.urls import reverse_lazy
from .models import Product

def send_mail_view(request):
    if request.method == 'GET':
        return render(request, 'email_sender.html')
    elif request.method == 'POST':
        email.delay(request.POST.get('message', 'Bos Mesaj'))
        return HttpResponse('<h1>Mail Gonderildi</h1>')

import dateutil.parser

def set_date(request):
    if request.method == 'GET':
        return render(request, 'time.html')
    elif request.method == 'POST':
        datetime = request.POST.get('datetime')
        clocked = ClockedSchedule.objects.create(clocked_time=datetime, enabled=True)
        PeriodicTask.objects.create(name="task"+datetime, task="app.tasks.sum", clocked=clocked, one_off=True, start_time=dateutil.parser.parse("2019-10-28 13:44:43"))
        return HttpResponse('<h1>Task Yaradildi</h1>')

def test_tags(request):
    return render(request, 'index.html', {
        'str':'slkdjflk sdokhf lsif skdf'
    })

class MyFormView(FormView):
    form_class = ProductForm
    template_name = 'form_test.html'
    success_url = reverse_lazy('test_tags')

def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {
        'products': products,
    })