from django.conf.urls import url, include
from rest_framework.documentation import include_docs_urls
from django.http.response import HttpResponse

urlpatterns = [
    url(r'^docs/', include_docs_urls(title='My API')),
    url(r'^v1/', include('main.urls')),
    url(r'^status', lambda request: HttpResponse("Working", status=200, content_type="text/plain"))
]
