from django.urls import path
from django import views
from . import views
# from django.conf import settings

urlpatterns = [
# path('cover/', views.base, name='base'),
path('index/', views.index, name='index'),
path('registraion/', views.login, name='login'),
path('show-index/', views.show_index, name = 'show_index'),
path('vote-index/',views.main,name='main'),
path('<int:question_id>/', views.detail, name='detail'),
path('<int:question_id>/results/', views.results, name='results'),
path('<int:question_id>/vote/', views.vote, name='vote'),
]

