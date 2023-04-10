from django.urls import path
from base.views import *


urlpatterns = [
    path('homepage/', HomePageView.as_view()),
    path('addhomepage/', HomePageView.as_view()),
    path('edithomepage/<int:home_id>/', HomePageView.as_view()),
    path('deletehomepage/<int:home_id>/', HomePageView.as_view()),
    path('contactus/', ContactusView.as_view()),
    path('addcotactus/', ContactusView.as_view()),
    path('editcontactus/<int:contact_id>/', ContactusView.as_view()),
    path('deletecontact/<int:contact_id>/', ContactusView.as_view()),
]
