from django.contrib import admin
from django.urls import path, include
from ironmon_stats import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'runs', views.RunViewSet)
router.register(r'pokemon', views.PokemonViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
