from django.contrib import admin
from django.urls import path
from ironmon_stats import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/runs/', views.RunList.as_view()),
    path('api/runs/<int:pk>/', views.RunDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
