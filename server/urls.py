from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from users.views import UserViewSet
from cars.views import CarBrandView, CarModelView, CarModificationView, CarSpecificationsView, PersonalCarView
from jobs.views import JobListView, JobOnCarView
from feedback.views import FeedbackView

router = routers.DefaultRouter()
router.register(**CarBrandView.router_path())
router.register(**CarModelView.router_path())
router.register(**CarModificationView.router_path())
router.register(**CarSpecificationsView.router_path())
router.register(**PersonalCarView.router_path())
router.register(**JobListView.router_path())

router.register(**UserViewSet.router_path())
router.register(**PersonalCarView.router_path())
router.register(**JobOnCarView.router_path())

router.register(**FeedbackView.router_path())

from users.views import CreateUserAPIView
router.register(r'u', CreateUserAPIView)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework')),
    path('auth/', include('rest_framework_social_oauth2.urls')),
    path('', include(router.urls)),
    # path('users/', include('users.urls', namespace='users')),
]

try:
    from rest_framework.documentation import include_docs_urls
    from django.conf.urls import url
    urlpatterns.append(url(r'^docs/', include_docs_urls(title='Status Car')))
except AssertionError:
    pass