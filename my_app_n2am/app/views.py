from django.shortcuts import render
from .models import Member

def index(request):
    obj=Member.objects.all()
    context = {
        'obj': obj
    }
    return render(request, "index.html",context)