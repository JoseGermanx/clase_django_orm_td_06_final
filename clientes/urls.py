from django.urls import path
from .views import ClienteListView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView

urlpatterns = [
    path('', ClienteListView.as_view(), name='cliente_list'),
    path('nuevo/', ClienteCreateView.as_view(), name='cliente_create'),
    path('editar/<int:pk>', ClienteUpdateView.as_view(), name='cliente_update'),
    path('eliminar/<int:pk>', ClienteDeleteView.as_view(), name='cliente_delete')
]