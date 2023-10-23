from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    password = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_trainer = models.BooleanField(default=False)

    REQUIRED_FIELDS = []


class Gym(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name


class Trainer(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    gym = models.OneToOneField(Gym, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class WorkoutSession(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    date = models.DateField()
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.client.name}'s session with {self.trainer.name} on {self.date}"
