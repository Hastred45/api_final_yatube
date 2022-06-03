from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if (request.method in permissions.SAFE_METHODS
                or obj.author == request.user):
            return True
