from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import ExpenseListCreateAPIView, ExpenseDetailAPIView

urlpatterns = [
    path("health/", ExpenseListCreateAPIView.as_view()),
    path("health/<int:pk>/", ExpenseDetailAPIView.as_view()),
    
    # "Login" endpoint
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
