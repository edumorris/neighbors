 
from django.shortcuts import render
# from .serializer import 
from rest_framework import status
from .permissions import IsAdminOrReadOnly

# Create your views here.
# Testpage
def index_test(request):
    title = "Iper testpage"

    return render(request, 'index.html', {"title": title})