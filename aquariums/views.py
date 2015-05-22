from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from aquariums.models import Analysis, Aquarium, AnalysisForm, AquariumForm, FishForm

def analysis(request, aquarium_id):
    p = get_object_or_404(Aquarium, pk=aquarium_id)
    if request.method == 'POST':
        form = AnalysisForm(request.POST)
        if form.is_valid():
            form_temp = form.save(commit=False)
            form_temp.aquarium_id = aquarium_id
            form_temp.save()
            return HttpResponseRedirect(reverse('aquariums:detail', args=(p.id,)))
    else:
        form = AnalysisForm()
    return render(request, 'aquariums/analysis_add.html', {'aquarium': p, 'form': form})
    
def fish(request, aquarium_id):
    p = get_object_or_404(Aquarium, pk=aquarium_id)
    if request.method == 'POST':
        form = FishForm(request.POST)
        if form.is_valid():
            form_temp = form.save(commit=False)
            form_temp.aquarium_id = aquarium_id
            form_temp.save()
            return HttpResponseRedirect(reverse('aquariums:detail', args=(p.id,)))
    else:
        form = FishForm()
    return render(request, 'aquariums/fish_add.html', {'aquarium': p, 'form': form})
    
def new(request):
    if request.method == 'POST':
        form = AquariumForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = AquariumForm()
    return render(request, 'aquariums/new.html', {'form': form})

        
