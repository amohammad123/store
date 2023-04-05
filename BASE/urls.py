from django.urls import path
from base.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('aboutus/', aboutusViwe),
    path('homepage/', homepageViwe),
    path('ticket/', ticketViwe),
    path('profile/<int:user_id>/', profileViwe),
    path('contactus/', contactusViwe),
    path('sendticket/', ticketeditViwe),
]

# see Media in debug=True:
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#or from BASE import viwe
# urlpatterns = [
#     path('aboutus', views.aboutusViwe),
#     path('homepage', views.homepageViwe),
#     path('ticket', views.ticketViwe),
#     path('user/<int:user_id>', views.userViwe),
#     path('contactus', views.contactusViwe)
# ]
