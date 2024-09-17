from django.shortcuts import render

from kis.models import Cadet


def main(request):
    return render(request, 'kis/main.html')


def main2(request):
    return render(request, 'kis/main2.html')


def cadet_list(request):
    cadet_list = Cadet.objects.all()
    return render(request, 'kis/cadet/list.html', {'cadet_list': cadet_list})


def add_cadet(request):
    return render(request, 'kis/cadet/add-form.html')
