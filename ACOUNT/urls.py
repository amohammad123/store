from django.urls import path
from ACOUNT.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', Login.as_view()),
    path('logout/', logoutView),
    path('profile/', ProfileView),
    path('signin/', profileRegisterViwe),
    path('editprofile/', profileEditViwe)

]

# see Media in debug=True:
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)