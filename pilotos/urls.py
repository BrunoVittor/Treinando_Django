from cadastro_de_pilotos import urls
from django.urls import path
from .views import pilots_list, pilots_new, pilots_update, pilots_delete


urlpatterns = [
    path('pilot/', pilots_list, name='pilots_list'),
    path('create', pilots_new, name='pilots_new'),
    path('update/<int:id>', pilots_update, name='pilots_update'),
    path('delete/<int:id>', pilots_delete, name='pilots_delete'),
]
