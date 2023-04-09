from account.forms import *
from account.models import *
from account.serializers import *
from rest_framework import status
from django.shortcuts import render
from django.db import IntegrityError
from rest_framework.views import APIView
from rest_framework.response import Response


class AutheView(APIView):
    def get(self, request, user_id=None):
        if request.user.is_staff:
            if user_id is None:
                return Response({"message": "User with this profile was not found!"},
                                status=status.HTTP_400_BAD_REQUEST)

            user = Profile.objects.get(user_id=user_id)
            user = ProfileSerializer(user).data

            return Response(user, status=status.HTTP_302_FOUND)
        else:
            user = Profile.objects.get(user_id=request.user.id)
            user = ProfileSerializer(user).data
            context = {
                "massege": "access denied",
                "your profile": user
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            user = User.objects.create_user(username=request.data["username"], password=request.data["password"])
            Profile.objects.create(user_id=user.id)
            user = UserSerializer(user).data

            return Response(user, status=status.HTTP_201_CREATED)
        except IntegrityError:
            return Response({"error": "username already exists"}, status=status.HTTP_409_CONFLICT)
        except Exception as err:
            return Response({'error': str(err)}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):

        if request.user and request.user.is_authenticated:
            user = User.objects.filter(id=request.user.id).update(**request.data)
            user = User.objects.get(id=request.user.id)
            user = UserSerializer(user).data

            return Response(user, status=status.HTTP_200_OK)
        else:
            return Response({"message": "access denied"}, status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request):
        if request.user.is_staff:
            try:
                user = User.objects.get(id=request.data["id"])
                user.delete()
                return Response({"message": "user {} deleted successfully".format(request.data["id"])},
                                status=status.HTTP_200_OK)
            except:
                return Response({"message": "user {} not exist".format(request.data["id"])},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "access denied"}, status=status.HTTP_400_BAD_REQUEST)
