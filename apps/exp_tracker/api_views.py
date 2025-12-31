from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import ExpenseSerializer

class HealthCheckAPIView(APIView):
    def get(self, request):
        return Response({"message": "GET is allowed"})
    
    def post(self, request):
        serializer = ExpenseSerializer(data=request.data)

        if serializer.is_valid():
            return Response(
                {
                    "validated_data": serializer.validated_data
                },
                status=status.HTTP_200_OK
            )
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )