from django.contrib import admin
from .models import Gym,WorkoutSession,Client,Trainer
# Register your models here.
admin.site.register(Gym)
admin.site.register(WorkoutSession)
admin.site.register(Trainer)
admin.site.register(Client)