# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Brand
from .serializers import BrandSerializer

class BrandDetails(APIView):
    def get(self, request, name):
        try:
            product = Brand.objects.get(name = name)
            serializer = BrandSerializer(product)
            return Response(serializer.data)
        except Brand.DoesNotExist:
            return Response({"message": "Brand not found"}, status=status.HTTP_404_NOT_FOUND)
