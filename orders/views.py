from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from . import serializers
from .models import Order


# Create your views here.

class HelloOrderView(generics.GenericAPIView):
    def get(self, request):
        return Response(data={"message": "Hello Order"}, status=status.HTTP_200_OK)

# view to list and create
class OrderCreateListView(generics.GenericAPIView):

    serializer_class = serializers.OrderCreationSerializer
    queryset = Order.objects.all()

    def get(self, request):

        orders = Order.objects.all()

        serializer = self.serializer_class(instance=orders, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        pass


# view for updating, deleting and getting one order
class OrderDetailView(generics.GenericAPIView):

    def get(self, request, order_id):
        pass


    def put(self, request, order_id):
        pass

    def delete(self, request, order_id):
        pass
