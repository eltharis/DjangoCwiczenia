from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from seresults_api import views

router = routers.DefaultRouter()
router.register(r'requests', views.SearchRequestViewSet)

urlpatterns = [
    # url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^token-auth/', obtain_auth_token),
    url(r'^users/$', views.user_list, name="user-list"),
    url(r'^', include(router.urls)),
]

