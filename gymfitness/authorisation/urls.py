from django.urls import path,include
from authorisation import views
from rest_framework.routers import DefaultRouter
from .views import GymViewSet, TrainerViewSet, ClientViewSet, WorkoutSessionViewSet, UserRegistration

router = DefaultRouter()
router.register(r'gyms', GymViewSet, basename='gym')
router.register(r'trainers', TrainerViewSet, basename='trainers')
router.register(r'clients', ClientViewSet, basename='clients')
router.register(r'sessions', WorkoutSessionViewSet, basename='workout-sessions')


urlpatterns = [
    path('api/', include(router.urls)),
    path('api/register/', UserRegistration.as_view(), name="sign-up")
]