from django.shortcuts import render

#APIs
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Neighborhood, Business
from .serializer import HoodSerializer
from rest_framework import status

#API security
from .permissions import IsAdminOrReadOnly

# Create your views here.

# Testpage
def index_test(request):
    title = "Iper testpage"

    return render(request, 'index.html', {"title": title})

# Business Search
def business_search(request):
    title = "Search Results"
    
    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_business = Business.objects.filter(business_name__icontains=search_term)

        return render(request, 'business_search.html', {"title": title, "businesses": searched_business})
    else:
        message = "No search term added"
        return render(request, 'business_search.html', {"title": title, "message": message})

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