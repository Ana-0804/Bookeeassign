from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    USER_TYPES = (
        ('trainer', 'Trainer'),
        ('client', 'Client'),
    )
    user_type = models.CharField(max_length=7, choices=USER_TYPES)

    def __str__(self):
        return self.username


class Gym(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name


class Trainer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    specialization = models.CharField(max_length=100)
    gym = models.OneToOneField(Gym, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class Client(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField(null=True)

    def __str__(self):
        return self.name

class WorkoutSession(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    date = models.DateField()
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.client.name}'s session with {self.trainer.name} on {self.date}"
