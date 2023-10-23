from rest_framework import permissions

class IsTrainerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.user_type == 'trainer' and request.method in permissions.SAFE_METHODS:
            return True
        elif request.user.user_type == 'trainer':
            return True
        return False
