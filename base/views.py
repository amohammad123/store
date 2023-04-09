from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework.views import APIView
import base.views
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from account.models import *
from django.contrib.auth.decorators import login_required
from account.forms import *
from .serializers import *
from django.db import IntegrityError
from app.authenticate import Authenticate



class AutheView(APIView):
    # permission_classes = (Authenticate,)
    def get(self, request, user_id=None):
        if request.user.is_staff:
            if user_id is None:
                return Response({"message": "User with this profile was not found!"},
                                status=status.HTTP_400_BAD_REQUEST)

            user = Profile.objects.get(user_id=user_id)
            user_serializer = UserSerializer(user).data

            return Response(user_serializer, status=status.HTTP_302_FOUND)
        else:
            # user = Profile.objects.get(id=request.user.id)           # error: permission

            return Response({"message": "access denied"}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            user = User.objects.create_user(username=request.data["username"], password=request.data["password"])
            profileModel = Profile.objects.create(user_id=user.id)
            user = UserSerializer(profileModel).data

            return Response(user, status=status.HTTP_201_CREATED)
        except IntegrityError:
            return Response({"error": "username already exists"}, status=status.HTTP_409_CONFLICT)
        except Exception as err:
            return Response({'error': str(err)}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, req):

        if req.user and req.user.is_authenticated:
            user = User.objects.filter(id=req.user.id).update(**req.data)
            user = User.objects.get(id=req.user.id)
            user = UserSerializer(user).data

            return Response(user, status=status.HTTP_200_OK)
        else:
            return Response({"message": "access denied"}, status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request):
        if request.user.is_staff:
            try:
                user = User.objects.get(id=request.data["id"])
                # user.delete()
                return Response({"message": "user {} deleted successfully".format(request.data["id"])},
                                status=status.HTTP_200_OK)
            except:
                return Response({"message": "user {} not exist".format(request.data["id"])},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "access denied"}, status=status.HTTP_400_BAD_REQUEST)


# class Login(APIView):
    # def get(self, request):
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     user = authenticate(request, username=username, password=password)
    #     serializer = UserSerializer(data=user)
    #     data = {}
    #     if user is not None:
    #         login(request, user)
    #         userserializer = serializer.save()
    #         data['message'] = 'login secsessfully!'
    #         data['token'] = Token.objects.get(user=userserializer).key
    #         if request.GET.get('next'):
    #             return HttpResponseRedirect(request.GET.get('next'))
    #         return Response(data, status=status.HTTP_200_OK)
    #     else:
    #         data = {
    #             'username': username,
    #             'errorMessege': "کاربری با این مشخصات یافت نشد"
    #         }
    #         return render(request, 'account/login.html', data)
    #         # return Response(data, status=status.HTTP_400_BAD_REQUEST)

    # @login_required()
    # def ProfileView(request):
    #     profile = request.user.profile
    #
    #     context = {
    #         "profilelist": profile
    #     }
    #
    #     return render(request, 'account/profile.html', context)
    #
    # def profileRegisterViwe(request):
    #     if request.method == "POST":
    #         profileRegister = ProfileRegister(request.POST, request.FILES)
    #         if profileRegister.is_valid():
    #             user = User.objects.create_user(username=profileRegister.cleaned_data['username'],
    #                                             email=profileRegister.cleaned_data['email'],
    #                                             password=profileRegister.cleaned_data['password'],
    #                                             first_name=profileRegister.cleaned_data['first_name'],
    #                                             last_name=profileRegister.cleaned_data['last_name'])
    #             user.save()
    #             profileModel = Profile(user=user, profileImage=profileRegister.cleaned_data['profileImage'],
    #                                    gender=profileRegister.clened_data['gender'],
    #                                    bornDate=profileRegister.cleaned_data['bornDate'],
    #                                    credit=profileRegister.cleaned_data['credit'])
    #             profileModel.save()
    #             return HttpResponseRedirect(reverse(base.views.homepageViwe))
    #     else:
    #         profileRegister = ProfileRegister()
    #
    #     context = {
    #         "formData": profileRegister
    #     }
    #     return render(request, 'account/profileregister.html', context)
    #
    # def profileEditViwe(request):
    #     if request.method == 'POST':
    #         profileEdit = ProfileEdit(request.POST, request.FILES, instance=request.user.profile)
    #         usetEdit = UserEdit(request.POST, instance=request.user)
    #         if profileEdit.is_valid() and usetEdit.is_valid():
    #             profileEdit.save()
    #             usetEdit.save()
    #             return HttpResponseRedirect(reverse(ProfileView))
    #     else:
    #         profileEdit = ProfileEdit(instance=request.user.profile)
    #         usetEdit = UserEdit(instance=request.user)
    #
    #     context = {
    #         "profileEdit": profileEdit,
    #         "userEdit": usetEdit,
    #         'profileImage': request.user.profile.profileImage
    #     }
    #     return render(request, 'account/profileedit.html', context)

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

