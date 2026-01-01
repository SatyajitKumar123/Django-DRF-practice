from django.urls import path
# from .views import HealthAPIView
from .views import ExpenseListCreateAPIView

urlpatterns = [
    path("health/", ExpenseListCreateAPIView.as_view()),
]
