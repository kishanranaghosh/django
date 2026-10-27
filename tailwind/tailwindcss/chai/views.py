

from django.shortcuts import render
from .models import ChaiVarity
from .forms import ChaiVarityForm

# Create your views here.
def all_chai(request):
    chais = ChaiVarity.objects.all()
    return render(request, 'chai/all_chai.html', {'chais': chais})

def chai_stores_view(request):
    stores = None
    if request.method == 'POST':
        form = ChaiVarityForm(request.POST)
        if form.is_valid():
            selected_varity = form.cleaned_data['chai_varity']
            stores = Store.objects.filter(chai_varity=selected_varity)
            



    return render(request, 'chai/chai_stores.html', {'stores': stores})