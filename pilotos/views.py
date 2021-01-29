from django.shortcuts import render, redirect, get_object_or_404
from .models import Pilot
from .forms import PilotForm


def pilots_list(request):
    context = {
        'pilots': Pilot.objects.all()
    }
    return render(request, 'list_of_pilots.html', context)


def pilots_new(request):
    forms = PilotForm(request.POST or None)
    if forms.is_valid():
        forms.save()
        return redirect('pilots_list')
    return render(request, 'pilot_forms.html', {'forms': forms})


def pilots_update(request, id):
    pilots = get_object_or_404(Pilot, pk=id)
    forms = PilotForm(request.POST or None, instance=pilots)
    if forms.is_valid():
        forms.save()
        return redirect('pilots_list')
    return render(request, 'pilot_forms.html', {'forms': forms})


def pilots_delete(request, id):
    pilots = get_object_or_404(Pilot, pk=id)
    forms = PilotForm(request.POST or None, instance=pilots)
    if request.method == 'POST':
        pilots.delete()
        return redirect('pilots_list')
    return render(request, 'pilot_delete.html', {'forms': forms})
