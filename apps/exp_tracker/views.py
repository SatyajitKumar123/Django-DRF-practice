from rest_framework import generics
from .models import Category, Expense
from .serializers import CategorySerializer, ExpenseSerializer


class CategoryListCreateView(generics.ListCreateAPIView):
    """  
    GET: Returns a list of all categories.
    POST: Creates a new category.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class ExpenseListCreateView(generics.ListCreateAPIView):
    """ 
    GET: Returns a list of all expenses.
    POST: Creates a new expense.
    """
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    
    def perform_create(self, serializer):
        serializer.save(user_id=1)