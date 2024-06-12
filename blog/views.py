from django.shortcuts import render
from .models import cardAdd, infoAdd
# Create your views here.
def index(request):
    return render(request, 'index.html', context={'info': infoAdd.objects.all(), 'card': cardAdd.objects.all()})

