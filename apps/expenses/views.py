from rest_framework.views import APIView
from rest_framework.response import Response


class HealthAPIView(APIView):
    def get(self, request):
        print("REQUEST CLASS:", type(request))
        print("METHOD:", request.method)
        print("QUERY PARAMS:", request.query_params)
        print("USER:", request.user)
        
        
        return Response({
            "status": "ok",
            "message": "Inspect DRF request in terminal"
        })