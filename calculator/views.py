from django.shortcuts import render
import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .forms import NameForm


def index(request):
    x = "<h3>Presciption can be sold on or after</h3>"
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            sold_date = form.cleaned_data['sold_date']
            days_early = form.cleaned_data['days_early']
            days_supply = form.cleaned_data['days_supply']
            earliest = sold_date + \
                datetime.timedelta(days=days_supply-days_early)
        return render(request, 'calculator/index.html', {'form': form, 'earliest': earliest.strftime("%m/%d/%Y"), "x": x})
    else:
        form = NameForm()
    return render(request, 'calculator/index.html', {'form': form})
