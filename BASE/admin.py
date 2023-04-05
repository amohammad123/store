from django.contrib import admin

from BASE.models import HomeSetting
from BASE.models import Aboutus
from BASE.models import Contactus
from BASE.models import Ticket
from BASE.models import Images
from BASE.models import Socialmedia


admin.site.register(HomeSetting)
admin.site.register(Aboutus)
admin.site.register(Contactus)
admin.site.register(Ticket)
admin.site.register(Images)
admin.site.register(Socialmedia)