from django.shortcuts import render
from .models import Todo
from rest_framework import generics
from .serializers import TodoSerializer


class TodoCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new Todo
	queryset = Todo.objects.all(),
	serializer_class = TodoSerializer


class TodoList(generics.ListAPIView):
    # API endpoint that allows Todo to be viewed.
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single Todo by pk.
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a Todo record to be updated.
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a Todo record to be deleted.
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer






