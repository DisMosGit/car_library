from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import mixins

from server.mixins import ViewRouterMixin
from .models import Feedback
from .serializers import FeedbackSerializer
from .telegram_bot import Bot
from server.settings import TELEGRAM_NOTIFICATIONS


class FeedbackView(mixins.CreateModelMixin, viewsets.GenericViewSet, ViewRouterMixin):
    router_prefix: str = r'feedback'
    router_basename: str = 'feedback'
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return []

    def perform_create(self, serializer):
        bot = Bot(TELEGRAM_NOTIFICATIONS['bot_key'], TELEGRAM_NOTIFICATIONS['users'])
        bot.form_and_send(user_id=self.request.user.id,
                          user_name=self.request.user.username,
                          title=serializer.data['title'],
                          text=serializer.data['text'],
                          datetime=serializer.data['datetime'])
