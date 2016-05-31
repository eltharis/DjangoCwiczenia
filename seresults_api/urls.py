from django.conf.urls import url, include
from rest_framework import routers

from seresults_api import views

router = routers.DefaultRouter()
router.register(r'requests', views.SearchRequestViewSet)

urlpatterns = [
    url(r'^users/$', views.user_list, name="user-list"),
    url(r'^', include(router.urls)),
]

