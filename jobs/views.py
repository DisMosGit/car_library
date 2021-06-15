from rest_framework import permissions
from rest_framework import viewsets

from server.mixins import ViewRouterMixin, FilterMixin
from .models import JobList, JobOnCar
from .serializers import JobListSerializer, JobOnCarSerializer
from .permissions import IsCarDriverOrOwner
from cars.models import PersonalCar


class JobListView(FilterMixin, ViewRouterMixin, viewsets.ReadOnlyModelViewSet):
    router_prefix: str = r'job/list'
    router_basename: str = 'job_list'
    model = JobList
    serializer_class = JobListSerializer
    permission_classes = [permissions.AllowAny]
    search_fields = ['name']


class JobOnCarView(FilterMixin, ViewRouterMixin, viewsets.ModelViewSet):
    router_prefix: str = r'my/jobs'
    router_basename: str = 'my_jobs'
    model = JobOnCar
    serializer_class = JobOnCarSerializer
    permission_classes = [permissions.IsAuthenticated, IsCarDriverOrOwner]
    search_fields = [
        'job__name__contains', 'job__id', 'user__name__contains', 'user__id',
        'car__name__contains', 'car__id', 'datetime__year', 'datetime__month',
        'datetime__day', 'datetime__gte', 'datetime__lte',
        'cost__gte', 'cost__lte'
    ]

    def get_queryset(self):
        queryset_cars = (PersonalCar.objects.filter(owner=self.request.user)
                         | self.request.user.driven.all()).distinct()
        filters = self.get_filter_params()
        if filters:
            queryset = JobOnCar.objects.filter(car__in=queryset_cars,
                                               **filters)
        else:
            queryset = JobOnCar.objects.filter(car__in=queryset_cars)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
