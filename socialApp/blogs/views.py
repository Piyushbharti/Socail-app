from django.shortcuts import render
from rest_framework import generics, status
from .models import Blog, comment
from .serializers import blogSerializer, CommentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from userAuth.pagination import CustomPagination
from .filter import BlogFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
@api_view(['GET'])
def getBlogById(request, pk):
    
    try:
        getBlog = Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        return Response({
            "status": status.HTTP_404_NOT_FOUND,
            "msg": "Blog Not Found",
            "data": []
        })
    serializer = blogSerializer(getBlog)
    return Response({"status": status.HTTP_200_OK, "msg": "Blog Found Success", "data" : serializer.data})


class BlogOperations(generics.ListCreateAPIView):
    queryset = Blog.objects.all() # isme v queryset likhna jaruri
    serializer_class = blogSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = BlogFilter
    search_fields = ['blog_title']
    ordering_fields = ['id']
    
class commentOperations(generics.ListCreateAPIView):
    queryset = comment.objects.all()
    serializer_class = CommentSerializer
    
class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = blogSerializer
    lookup_field="pk"
    
class commentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = "pk"