from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner

from .models import Expense
from .serializers import ExpenseSerializer


class ExpenseListCreateAPIView(ListCreateAPIView):
    
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
class ExpenseDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)