from django.urls import path
from base.views import *
from django.conf import settings


urlpatterns = [
    path('homepage/', HomePage.as_view()),
    path('addhomepage/', HomePage.as_view()),
    path('edithomepage/<int:home_id>/', HomePage.as_view()),
    path('deletehomepage/<int:home_id>/', HomePage.as_view()),
    # path('aboutus/', aboutusViwe),
    # path('homepage/', homepageViwe),
    # path('ticket/', ticketViwe),
    # path('profile/<int:user_id>/', profileViwe),
    # path('contactus/', contactusViwe),
    # path('sendticket/', ticketeditViwe),
]
