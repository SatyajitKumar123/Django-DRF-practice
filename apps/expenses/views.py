from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import ExpenseSerializer


class HealthAPIView(APIView):
    def post(self, request):
        serializer = ExpenseSerializer(data=request.data)

        if not serializer.is_valid():
              return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

        return Response(serializer.data)