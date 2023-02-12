from rest_framework.permissions import BasePermission, IsAdminUser, SAFE_METHODS, DjangoModelPermissionsOrAnonReadOnly


class IsAuthenticatedOwner(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        # OOP
        # 4 +  object, class
        if hasattr(obj, 'user') and request.user == obj.user:
            return True
        return False


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user and request.user.is_authenticated and request.method in SAFE_METHODS or request.user.is_staff
        )


class IsShopOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS or hasattr(obj, 'user') and request.user and request.user == obj.user:
            return True
        return False
