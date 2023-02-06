from rest_framework.permissions import BasePermission, IsAdminUser, SAFE_METHODS


class IsAuthenticatedOwner(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated or request.user.is_staff)

    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True
        return False


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user and request.user.is_authenticated and request.method in SAFE_METHODS or request.user.is_staff
        )


# class