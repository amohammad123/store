from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from BASE.models import *
from ACOUNT.models import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from BASE.forms import *


def aboutusViwe(request):
    aboutus = Aboutus.objects.all()
    contex = {
        "aboutuslist": aboutus,
        "count": aboutus.count()
    }
    # text= """
    # <!DOCTYPE html>
    # <html>
    #     <head></head>
    #     <body>
    #         <h1> درباره ما <h1>
    #         <ul>
    #             {}
    #         <ul>
    #     </body>
    # </html>
    #
    # """ .format('\n'.join('<li>{}<li>'.format(about) for about in aboutus))
    return render(request, "BASE/aboutus.html", contex)


def homepageViwe(request):

    searchform = Search(request.GET)
    if searchform.is_valid():
        searchtext = searchform.cleaned_data["searchtext"]
        home = HomeSetting.objects.filter(superiority__contains=searchtext)

    else:
        home = HomeSetting.objects.all()

    contex = {
        "homelist": home,
        "searchform": searchform
    }

    return render(request, "BASE/homepage.html", contex)





@login_required()
def ticketViwe(request):
    # if request.user.is_staff and request.user.is_active:
        ticket = Ticket.objects.all()
        contex = {
            "ticketlist": ticket,
        }

        return render(request, "BASE/ticket.html", contex)
    # else:
    #     return HttpResponseRedirect(reverse(ACOUNT.views.loginView))

def profileViwe(request, user_id):
    user = Profile.objects.get(pk=user_id)
    contex = {
        "userlist": user
    }
    return render(request, "BASE/user.html", contex)


def contactusViwe(request):
    contactus = Contactus.objects.all()
    contex = {
        "contactuslist": contactus,
    }

    return render(request, "BASE/contactus.html", contex)

def ticketeditViwe(request):
    # ticketform = TicketEd(request.GET)
    # sendticket = ticketform(request.POST, instance=ticketform)
    if request.method == "POST":
        sendticket = TicketEd(request.POST)
        if sendticket.is_valid():
            sendticket.save()
            return HttpResponseRedirect(reverse(ticketViwe))

    contex = {
        "sendticket": sendticket,
    }

    return render(request, "BASE/ticketedit.html", contex)
