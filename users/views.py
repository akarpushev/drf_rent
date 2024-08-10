from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer, LoginSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework import status

User = get_user_model()


class RegisterUserView(generics.CreateAPIView):
    # permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

    # если нужно переопределить
    # def post(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)


class LoginUserView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        # username = request.data.get('username')
        # password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return Response('ok')

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
