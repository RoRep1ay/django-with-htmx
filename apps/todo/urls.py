from django.urls import path
from .views import home, create, update, validate

app_name = 'todo'

urlpatterns = [
    path('', home, name='home'),
    path('todos/', create, name='create'),
    path('todos/validate/', validate, name='validate'),
    path('todos/<int:id>/', update, name='update'),
]
