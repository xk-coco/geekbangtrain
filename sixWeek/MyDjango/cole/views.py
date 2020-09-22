from django.shortcuts import render, redirect
from .models import Name

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello Django!")


# path('<int:year>', views.year)
def year(request, year):
    # return HttpResponse(year)
    return redirect('/2020.html')


# path('<str:name>/<int:year>', views.name),
def nameandyear(request, **kwargs):
    return HttpResponse(kwargs['name'] + str(kwargs['year']))


# path('<myint:year>', views.year),
# re_path('(?P<year>[0-9]{4}).html', views.myyear, name='urlyear'),
def myyear(request, year):
    return render(request, 'yearview.html')


def books(request):
    ### 从models取数据传给template  ###
    n = Name.objects.all()
    return render(request, 'bookslist.html', locals())  ### render()将本地文档与模板关联
