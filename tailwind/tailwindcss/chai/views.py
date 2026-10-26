from django.shortcuts import render
from .models import ChaiVarity

# Create your views here.
def all_chai(request):
    chais = ChaiVarity.objects.all()
    return render(request, 'chai/all_chai.html', {'chais': chais})

def chai_stores_view(request):
    return render(request, 'chai/chai_stores.html')