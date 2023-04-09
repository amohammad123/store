from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from base.models import *
from account.models import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from base.forms import *
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from .signals import *
from django.db import IntegrityError


class HomePage(APIView):
    def get(self, request):
        if HomeSetting.objects.count() > 0:
            try:
                homepage = HomeSetting.objects.all()
                homepage = HomeSerializer(homepage, many=True).data
                return Response(homepage, status=status.HTTP_200_OK)
            except:
                return Response({'massege': 'please try again'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'massege': 'there is no homepage data'}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        # permission_classes = (IsAdminUser,)
        if request.data["id"]:
            homeid = HomeSetting.objects.filter(id=request.data["id"]).count()
            if homeid == 0:
                try:
                    homepage = HomeSetting.objects.create(**request.data)
                    homepage = HomeSerializer(homepage).data
                    return Response(homepage, status=status.HTTP_201_CREATED)
                except:
                    return Response({'massege': 'please try again'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"error": "home_id: {}, already exists".format(request.data["id"])},
                                status=status.HTTP_409_CONFLICT)
        else:
            try:
                homepage = HomeSetting.objects.create(**request.data)
                homepage = HomeSerializer(homepage).data
                return Response(homepage, status=status.HTTP_201_CREATED)
            except:
                return Response({'massege': 'please try again'}, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, home_id):
        # permission_classes = (IsAdminUser,)
        try:
            homepage = HomeSetting.objects.filter(id=home_id)
            homepage = homepage.update(**request.data)
            try:
                homepage = HomeSetting.objects.get(id=request.data["id"])
            except:
                homepage = HomeSetting.objects.get(id=home_id)
            homepage = HomeSerializer(homepage).data
        except:
            homepage = HomeSetting.objects.all()
            homepage = HomeSerializer(homepage, many=True).data


        return Response(homepage, status=status.HTTP_200_OK)

    def delete(self, request, home_id):
        homefilter = HomeSetting.objects.filter(id=home_id).count()
        if homefilter > 0:
            homepage = HomeSetting.objects.get(id=home_id)
            homepage.delete()
            return Response({"massege": "home id: {}, deleted successfully".format(home_id)}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "home id: {} was not found!"},
                            status=status.HTTP_400_BAD_REQUEST)
# {
#     "slogan": "test edit slohgan 4",
#     "superiority": "test edit superiority 1"
# }
# def aboutusViwe(request):
#     aboutus = Aboutus.objects.all()
#     contex = {
#         "aboutuslist": aboutus,
#         "count": aboutus.count()
#     }
#     # text= """
#     # <!DOCTYPE html>
#     # <html>
#     #     <head></head>
#     #     <body>
#     #         <h1> درباره ما <h1>
#     #         <ul>
#     #             {}
#     #         <ul>
#     #     </body>
#     # </html>
#     #
#     # """ .format('\n'.join('<li>{}<li>'.format(about) for about in aboutus))
#     return render(request, "base/aboutus.html", contex)
#
#
# def homepageViwe(request):
#     searchform = Search(request.GET)
#     if searchform.is_valid():
#         searchtext = searchform.cleaned_data["searchtext"]
#         home = HomeSetting.objects.filter(superiority__contains=searchtext)
#
#     else:
#         home = HomeSetting.objects.all()
#
#     contex = {
#         "homelist": home,
#         "searchform": searchform
#     }
#
#     return render(request, "base/homepage.html", contex)
#
#
# @login_required()
# def ticketViwe(request):
#     # if request.user.is_staff and request.user.is_active:
#     ticket = Ticket.objects.all()
#     contex = {
#         "ticketlist": ticket,
#     }
#
#     return render(request, "base/ticket.html", contex)
#
#
# # else:
# #     return HttpResponseRedirect(reverse(account.views.loginView))
#
# def profileViwe(request, user_id):
#     user = Profile.objects.get(pk=user_id)
#     contex = {
#         "userlist": user
#     }
#     return render(request, "base/user.html", contex)
#
#
# def contactusViwe(request):
#     contactus = Contactus.objects.all()
#     contex = {
#         "contactuslist": contactus,
#     }
#
#     return render(request, "base/contactus.html", contex)
#
#
# def ticketeditViwe(request):
#     # ticketform = TicketEd(request.GET)
#     # sendticket = ticketform(request.POST, instance=ticketform)
#     if request.method == "POST":
#         sendticket = TicketEd(request.POST)
#         if sendticket.is_valid():
#             sendticket.save()
#             return HttpResponseRedirect(reverse(ticketViwe))
#
#     contex = {
#         "sendticket": sendticket,
#     }
#
#     return render(request, "base/ticketedit.html", contex)
