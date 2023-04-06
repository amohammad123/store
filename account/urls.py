from django.urls import path
from account.views import *
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', AutheView.as_view()),
    path('account/', AutheView.as_view()),
    path('login/', Login.as_view()),
    path('profile/<int:id>', AutheView.as_view()),
    # path('logout/', logoutView),
    # path('profile/', ProfileView),
    # path('signin/', profileRegisterViwe),
    # path('editprofile/', profileEditViwe)

]

# see Media in debug=True:
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
