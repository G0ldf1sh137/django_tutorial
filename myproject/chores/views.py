from django.http import HttpResponse
from django.shortcuts import render

# from .models import Post


def chores_day(request):
    return render(request, 'chores/chores_day.html')