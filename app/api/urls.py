from django.urls import path
from . import views

urlpatterns = [
    path('', ),
    path('solve_with_llm', views.solve_with_llm),
]