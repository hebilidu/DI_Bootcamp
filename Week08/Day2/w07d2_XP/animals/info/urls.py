from django.urls import path
from . import views

urlpatterns = [
    path('animal/<int:animal_id>', views.animal, name='animalpage'),
    path('family/<int:family_id>', views.family),
    path('animals/', views.animals)
]