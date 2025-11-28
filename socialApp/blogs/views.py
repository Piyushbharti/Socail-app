from django.shortcuts import render
from rest_framework import generics
from .models import Blog, comment
from .serializers import blogSerializer, CommentSerializer

# Create your views here.
class BlogOperations(generics.ListCreateAPIView):
    queryset = Blog.objects.all() # isme v queryset likhna jaruri
    serializer_class = blogSerializer
    
    
class commentOperations(generics.ListCreateAPIView):
    queryset = comment.objects.all()
    serializer_class = CommentSerializer