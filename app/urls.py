from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base', include('base.urls')),              # 'site name'
    path('', include('account.urls')),
    path('blog/', include('blog.urls')),
    path('store/', include('store.urls')),
]

# see Media in debug=True:
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
