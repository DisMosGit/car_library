from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import mixins

from server.mixins import ViewRouterMixin
from .permissions import IsUser
from .serializers import UserSerializer, CreateUserSerializer
from .models import User


class UserViewSet(viewsets.ReadOnlyModelViewSet, ViewRouterMixin):
    router_prefix: str = r'my/profile'
    router_basename: str = 'my_profile'
    model = User
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsUser]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

# Must remove
class CreateUserAPIView(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = CreateUserSerializer
    queryset = User.objects.all()
