from rest_framework import permissions


class AuthorOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if (
            request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated):
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if (
            request.method in permissions.SAFE_METHODS
                or obj.author == request.user):
            return True
        return False
