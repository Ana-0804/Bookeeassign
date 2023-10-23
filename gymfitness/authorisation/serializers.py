from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Gym, Trainer, Client, WorkoutSession, CustomUser

class CustomUserSerializer(serializers.Serializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'is_trainer']

    def create(self, validated_data):
        username = validated_data.get('username', None)
        password = validated_data.get('password', None)
        is_trainer = validated_data.get('is_trainer', None)
        specialization = validated_data.get('specialization', None)
        age = validated_data.get('age', None)
        hashed_password = make_password(password)
        existing_user = CustomUser.objects.filter(username=username).first()
        if existing_user:
            raise serializers.ValidationError({'username': 'This username is already in use.'})
        else:
            user = CustomUser.objects.create(password=hashed_password, **validated_data)

        if is_trainer == True:
            if specialization:
                Trainer.objects.create(user=user, specialization=specialization)
            else:
                raise serializers.ValidationError({'specialization': 'This field is required for Trainer registration.'})
        else:
            if age:
                Client.objects.create(user=user, specialization=specialization)
            else:
                raise serializers.ValidationError({'Age': 'This field is required for Trainer registration.'})
        return user


class GymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gym
        fields = '__all__'

class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class WorkoutSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutSession
        fields = '__all__'
