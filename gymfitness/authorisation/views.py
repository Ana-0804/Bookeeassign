from rest_framework import viewsets, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Gym, Trainer, Client, WorkoutSession,CustomUser
from .serializers import (GymSerializer, TrainerSerializer, ClientSerializer, WorkoutSessionSerializer,
                            CustomUserSerializer, MyTokenObtainPairSerializer)
from .permissions import IsTrainerOrReadOnly


class GymViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GymSerializer
    queryset = Gym.objects.all()


class TrainerViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TrainerSerializer
    queryset = Trainer.objects.all()


class ClientViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class WorkoutSessionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsTrainerOrReadOnly]
    serializer_class = WorkoutSessionSerializer
    queryset = WorkoutSession.objects.all()


class UserRegistration(APIView):
    def post(self, request, format='json'):
        data = request.data
        print(">>>>>> before", data["password"])
        data['password'] = make_password(data['password'])  # Hash the password
        print(">>>>>> after", data["password"])
        serializer = CustomUserSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
            if user.user_type == 'trainer':
                name = request.data.get("name",None)
                specialization = request.data.get("specialization", None)
                Trainer.objects.create(user=user, name=name, specialization=specialization)
            else:
                name = request.data.get("name",None)
                age = request.data.get("age", None)
                Client.objects.create(user=user, name=name, age=age)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MyTokenObtainPairView(TokenObtainPairView):
    """
    Arguments : request_data ["username","password"]
    Returns : tokens (refersh , access) and user_id
    """
    serializer_class = MyTokenObtainPairSerializer