from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from groups import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ranking/', include('groups.urls')),
    path('rankingjson/', views.HeroRanking.as_view()),
    path('defeatedheroeslist/', views.DefeatedHeroList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)