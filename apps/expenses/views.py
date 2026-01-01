from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Expense
from .serializers import ExpenseSerializer


class HealthAPIView(APIView):
    def get(self, request):
        expenses = Expense.objects.all()
        serializer = ExpenseSerializer(expenses, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ExpenseSerializer(data=request.data)

        if not serializer.is_valid():
              return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

        expense = serializer.save()
        
        return Response(
            ExpenseSerializer(expense).data,
            status=status.HTTP_201_CREATED
        )