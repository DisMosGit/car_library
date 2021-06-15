from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsOwnerOrDriverReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        elif request.method in permissions.SAFE_METHODS:
            return request.user in obj.drivers.all()
        else:
            return False


class IsDriver(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user in obj.driven.all()