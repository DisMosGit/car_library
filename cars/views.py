from rest_framework import permissions
from rest_framework import viewsets

from server.mixins import ViewRouterMixin, FilterMixin
from .permissions import IsOwnerOrDriverReadOnly
from .models import CarBrand, CarModel, CarModification, CarSpecifications, PersonalCar
from .serializers import CarBrandSerializer, CarModelSerializer, CarModificationSerializer, CarSpecificationsSerializer, PersonalCarSerializer


class CarBrandView(FilterMixin, ViewRouterMixin,
                   viewsets.ReadOnlyModelViewSet):
    router_prefix: str = r'cars/brands'
    router_basename: str = 'car_brands'
    model = CarBrand
    serializer_class = CarBrandSerializer
    permission_classes = [permissions.AllowAny]
    search_fields = ['brand__contains']


class CarModelView(FilterMixin, ViewRouterMixin,
                   viewsets.ReadOnlyModelViewSet):
    router_prefix: str = r'cars/models'
    router_basename: str = 'car_models'
    model = CarModel
    serializer_class = CarModelSerializer
    permission_classes = [permissions.AllowAny]
    search_fields = ['brand__id', 'brand__brand__contains', 'model__contains']


class CarModificationView(FilterMixin, ViewRouterMixin,
                          viewsets.ReadOnlyModelViewSet):
    router_prefix: str = r'cars/modifications'
    router_basename: str = 'car_modifications'
    model = CarModification
    serializer_class = CarModificationSerializer
    permission_classes = [permissions.AllowAny]
    search_fields = ['model__model__contains']


class CarSpecificationsView(FilterMixin, ViewRouterMixin,
                            viewsets.ReadOnlyModelViewSet):
    router_prefix: str = r'cars/specifications'
    router_basename: str = 'car_specifications'
    model = CarSpecifications
    serializer_class = CarSpecificationsSerializer
    permission_classes = [permissions.AllowAny]
    search_fields = ['brand__contains']


class PersonalCarView(viewsets.ModelViewSet, ViewRouterMixin):
    router_prefix: str = r'my/cars'
    router_basename: str = 'my_cars'
    model = PersonalCar
    serializer_class = PersonalCarSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrDriverReadOnly]

    def get_queryset(self):
        queryset = (PersonalCar.objects.filter(owner=self.request.user)
                    | self.request.user.driven.all()).distinct()
        return queryset

    def perform_create(self, serializer):
        # queryset.update(self.request.user.drivers.all())
        serializer.save(owner=self.request.user)
