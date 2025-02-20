from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.home, name='home'),
    path('solve/llm/<int:model_id>', views.solve_with_llm),
]