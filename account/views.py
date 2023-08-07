from django.shortcuts import render
from rest_framework import generics, serializers, status, permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializer import RegisterSerializer, LoginSerializer, MyProfileSerializer, MyProductCustomerSerializer, \
    MyProductSellerSerializer
from .models import Account, MyProduct
from .permission import IsOwnerReadOnly


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': True, 'data': 'Account successfully created'}, status=status.HTTP_201_CREATED)


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'tokens': serializer.data['tokens']}, status=status.HTTP_200_OK)


class MyProfileList(generics.ListAPIView):
    serializer_class = MyProfileSerializer
    queryset = Account.objects.all()
    permission_classes = [IsOwnerReadOnly]


class MySellerListCreate(generics.ListCreateAPIView):
    queryset = MyProduct.objects.all()
    serializer_class = MyProductSellerSerializer
    permission_classes = (IsAuthenticated, IsOwnerReadOnly)

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx['author'] = self.request.user
        return ctx


class MyCustomerList(generics.ListAPIView):
    queryset = MyProduct.objects.all()
    serializer_class = MyProductCustomerSerializer
    permission_classes = (IsOwnerReadOnly, IsAuthenticated)









