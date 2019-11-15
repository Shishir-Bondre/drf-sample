from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from django.urls import path

from main import views as main_api

router = routers.DefaultRouter()
router.register(r'things', main_api.ThingViewSet)

urlpatterns = [
	url(r'^', include(router.urls)),
	path('users/', main_api.UserViewSet.as_view()),
]
