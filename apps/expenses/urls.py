from django.urls import path
# from .views import HealthAPIView
from .views import ExpenseListCreateAPIView, ExpenseDetailAPIView

urlpatterns = [
    path("health/", ExpenseListCreateAPIView.as_view()),
    path("health/<int:pk>/", ExpenseDetailAPIView.as_view()),
]
