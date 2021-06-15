from rest_framework import permissions

# class IsCarOwner(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         return obj.car.owner == request.user


class IsCarDriverOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user in obj.car.drivers.all():
            return True
        return obj.car.owner == request.user
