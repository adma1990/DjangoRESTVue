from django.shortcuts import render
from rest_framework import viewsets
from .models import Blog
from .serializer import BlogSerializer
# Create


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

#