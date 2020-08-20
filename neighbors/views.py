from django.shortcuts import render

#APIs
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Neighborhood
from .serializer import HoodSerializer
from rest_framework import status

#API security
from .permissions import IsAdminOrReadOnly

# Create your views here.

# Testpage
def index_test(request):
    title = "Iper testpage"

    return render(request, 'index.html', {"title": title})

# API Classes
class Hoods(APIView):
    def get(self, request, format=None):
        all_hoods = Neighborhood.objects.all()
        serializers = HoodSerializer(all_hoods, many=True)
        return Response(serializers.data)
    
    def post(self, request, format=None):
        permission_classes = (IsAdminOrReadOnly,)
        serializers = HoodSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)