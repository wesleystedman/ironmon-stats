from django.contrib import admin
from django.urls import path, include
from ironmon_stats import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/runs/', views.RunList.as_view()),
    path('api/runs/<int:pk>/', views.RunDetail.as_view()),
    path('api/pokemon/', views.PokemonList.as_view()),
    path('api/pokemon/<int:pk>/', views.PokemonDetail.as_view()),
    path('api/users/', views.UserList.as_view()),
    path('api/users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
