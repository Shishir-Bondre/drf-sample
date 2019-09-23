from django.conf.urls import url, include
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    url(r'^docs/', include_docs_urls(title='My API')),
    url(r'^v1/', include('main.urls')),
]
