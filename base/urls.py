from django.urls import path
from base.views import *
from django.conf import settings


urlpatterns = [
    path('homepage/', HomePageView.as_view()),
    path('addhomepage/', HomePageView.as_view()),
    path('edithomepage/<int:home_id>/', HomePageView.as_view()),
    path('deletehomepage/<int:home_id>/', HomePageView.as_view()),
    path('contactus/', ContactusView.as_view()),
    path('addcotactus/', ContactusView.as_view()),
    path('editcontactus/<int:contact_id>/', ContactusView.as_view()),
    path('deletecontact/<int:contact_id>/', ContactusView.as_view()),

    # path('aboutus/', aboutusViwe),
    # path('homepage/', homepageViwe),
    # path('ticket/', ticketViwe),
    # path('profile/<int:user_id>/', profileViwe),
    # path('contactus/', contactusViwe),
    # path('sendticket/', ticketeditViwe),
]
