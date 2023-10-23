from rest_framework import viewsets, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Gym, Trainer, Client, WorkoutSession,CustomUser
from .serializers import (GymSerializer, TrainerSerializer, ClientSerializer, WorkoutSessionSerializer,
                            CustomUserSerializer)
from .permissions import IsTrainerOrReadOnly


class GymViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = GymSerializer
    queryset = Gym.objects.all()


class TrainerViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = TrainerSerializer
    queryset = Trainer.objects.all()


class ClientViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class WorkoutSessionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsTrainerOrReadOnly]
    serializer_class = WorkoutSessionSerializer
    queryset = WorkoutSession.objects.all()


class UserRegistration(APIView):
    """
    Arguments : API View, request_data
                request_data = ["username","email","password"]
    Returns : created user data (username & email)
    """
    def post(self, request):    
        serializer = CustomUserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)