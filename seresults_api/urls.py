from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from seresults_api import views

router = routers.DefaultRouter()
router.register(r'requests', views.SearchRequestViewSet)

urlpatterns = [
    url(r'^users/$', views.user_list, name="user-list"),
    url(r'^oauth/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^', include(router.urls)),
]

