from base.models import *
from account.models import *
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

