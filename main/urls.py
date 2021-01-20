from django.urls import path
from .views import index
from .views import by_rubric
from .views import detail

app_name = 'main'
urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/', by_rubric, name='by_rubric'),
    path('<int:rubric_pk>/<int:pk>/', detail, name='detail'),
]
