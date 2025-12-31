from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("apps.exp_tracker.urls")),
    path('api/v1/', include("apps.expenses.urls")),
]
