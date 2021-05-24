from django.shortcuts import render
from .models import Family, Animal

def animals(request):
    '''List all animals from db'''
    animal_list = Animal.objects.all()
    return render(request, 'animals.html', {'animal_list':animal_list})

def family(request, family_id):
    '''Display animals belonging to family designated by its id'''
    fam = Family.objects.get(id=family_id)
    animals = Animal.objects.filter(family=fam)
    # animals = fam.animal_set.all() # identique a la ligne precedente
    return render(request, 'family.html', {'family':fam, 'animals':animals})
        
def animal(request, animal_id):
    '''Display detailed info about animal designated by its id'''
    animal = Animal.objects.get(id=animal_id)
    return render(request,'animal.html', {'animal':animal})