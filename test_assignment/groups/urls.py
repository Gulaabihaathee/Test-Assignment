from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.ranking, name='ranking'),
    path('json/', views.HeroRanking.as_view()),
    path('defeatedheroeslist/', views.DefeatedHeroList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)