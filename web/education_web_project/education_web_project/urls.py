from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
	url(r'^admin/', admin.site.urls),
    url(r'^', include('index_page.urls')),
    url(r'^python/', include('python.urls')),
    url(r'^math/', include('math_scince.urls')),
]
