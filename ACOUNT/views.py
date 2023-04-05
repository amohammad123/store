from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework.views import APIView
import BASE.views
import basic_section.settings
from django.http import HttpResponse, HttpResponseRedirect
from BASE import views
from django.urls import reverse
from ACOUNT.models import *
from django.contrib.auth.decorators import login_required
from ACOUNT.forms import *
from .serializers import *
from rest_framework.authtoken.models import Token


class Login(APIView):
    def get(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        serializer = UserSerializer(data=user)
        data = {}
        if user is not None:
            login(request, user)
            userserializer = serializer.save()
            data['message'] = 'login secsessfully!'
            data['token'] = Token.objects.get(user=userserializer).key
            if request.GET.get('next'):
                return HttpResponseRedirect(request.GET.get('next'))
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = {
                'username': username,
                'errorMessege': "کاربری با این مشخصات یافت نشد"
            }
            return render(request, 'ACOUNT/login.html', data)
            # return Response(data, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):


def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse(BASE.views.homepageViwe))


@login_required()
def ProfileView(request):
    profile = request.user.profile

    context = {
        "profilelist": profile
    }

    return render(request, 'ACOUNT/profile.html', context)


def profileRegisterViwe(request):
    if request.method == "POST":
        profileRegister = ProfileRegister(request.POST, request.FILES)
        if profileRegister.is_valid():
            user = User.objects.create_user(username=profileRegister.cleaned_data['username'],
                                            email=profileRegister.cleaned_data['email'],
                                            password=profileRegister.cleaned_data['password'],
                                            first_name=profileRegister.cleaned_data['first_name'],
                                            last_name=profileRegister.cleaned_data['last_name'])
            user.save()
            profileModel = Profile(user=user, profileImage=profileRegister.cleaned_data['profileImage'],
                                   gender=profileRegister.clened_data['gender'],
                                   bornDate=profileRegister.cleaned_data['bornDate'],
                                   credit=profileRegister.cleaned_data['credit'])
            profileModel.save()
            return HttpResponseRedirect(reverse(BASE.views.homepageViwe))
    else:
        profileRegister = ProfileRegister()

    context = {
        "formData": profileRegister
    }
    return render(request, 'ACOUNT/profileregister.html', context)


def profileEditViwe(request):
    if request.method == 'POST':
        profileEdit = ProfileEdit(request.POST, request.FILES, instance=request.user.profile)
        usetEdit = UserEdit(request.POST, instance=request.user)
        if profileEdit.is_valid() and usetEdit.is_valid():
            profileEdit.save()
            usetEdit.save()
            return HttpResponseRedirect(reverse(ProfileView))
    else:
        profileEdit = ProfileEdit(instance=request.user.profile)
        usetEdit = UserEdit(instance=request.user)

    context = {
        "profileEdit": profileEdit,
        "userEdit": usetEdit,
        'profileImage': request.user.profile.profileImage
    }
    return render(request, 'ACOUNT/profileedit.html', context)
