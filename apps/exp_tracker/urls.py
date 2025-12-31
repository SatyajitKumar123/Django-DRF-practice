from django.urls import path
from .views import CategoryListCreateView, ExpenseListCreateView

urlpatterns = [
    path('api/categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('api/expense/', ExpenseListCreateView.as_view(), name='expense-list-create'),
]

