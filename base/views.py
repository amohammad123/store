from account.models import *
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from .signals import *


class HomePageView(APIView):
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
        try:
            if request.data["id"] and HomeSetting.objects.filter(id=request.data["id"]).count() > 0:
                homepage = HomeSetting.objects.all()
                homepage = HomeSerializer(homepage, many=True).data
                data = {
                    "massege": "id:{}, already exists".format(request.data["id"]),
                    "existdata": homepage
                }
                return Response(data, status=status.HTTP_409_CONFLICT)
            else:
                homepage = HomeSetting.objects.create(**request.data)
                homepage = HomeSerializer(homepage).data
                return Response(homepage, status=status.HTTP_201_CREATED)
        except:
            try:
                homepage = HomeSetting.objects.create(**request.data)
                homepage = HomeSerializer(homepage).data
                return Response(homepage, status=status.HTTP_201_CREATED)
            except:
                return Response({"massege": "please enter the correct objects"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, home_id):
        # permission_classes = (IsAdminUser,)
        try:
            homepage = HomeSetting.objects.filter(id=home_id)
            if homepage.exists():
                homepage.update(**request.data)
                homepage = HomeSetting.objects.get(id=home_id)
                homepage = HomeSerializer(homepage).data
                return Response(homepage, status=status.HTTP_200_OK)

            else:
                homepage = HomeSetting.objects.all()
                homepage = HomeSerializer(homepage, many=True).data
                data = {
                    "massege": "id:{}, not existsed".format(home_id),
                    "existdata": homepage
                }
                return Response(data, status=status.HTTP_409_CONFLICT)
        except:
            return Response({"massege": "please enter the correct objects"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, home_id):
        # permission_classes = (IsAdminUser,)
        homepage = HomeSetting.objects.filter(id=home_id)
        if homepage.count() > 0:
            homepage = HomeSetting.objects.get(id=home_id)
            homepage.delete()
            return Response({"massege": "id: {}, deleted successfully".format(home_id)}, status=status.HTTP_200_OK)

        else:
            homepage = HomeSetting.objects.all()
            homepage = HomeSerializer(homepage, many=True).data
            data = {
                "massege": "id:{}, was not found!".format(home_id),
                "existdata": homepage
            }
            return Response(data, status=status.HTTP_409_CONFLICT)


class ContactusView(APIView):
    def get(self, request):
        if Contactus.objects.count() > 0:
            try:
                contactus = Contactus.objects.all()
                contactus = ContactSerializer(contactus, many=True).data
                return Response(contactus, status=status.HTTP_200_OK)
            except:
                return Response({'massege': 'please try again'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'massege': 'there is no data'}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        # permission_classes = (IsAdminUser,)
        try:
            if request.data["id"] and Contactus.objects.filter(id=request.data["id"]).count() > 0:
                contactus = Contactus.objects.all()
                contactus = ContactSerializer(contactus, many=True).data
                data = {
                    "massege": "id:{}, already exists".format(request.data["id"]),
                    "existdata": contactus
                }
                return Response(data, status=status.HTTP_409_CONFLICT)
            else:
                contactus = Contactus.objects.create(**request.data)
                contactus = ContactSerializer(contactus).data
                return Response(contactus, status=status.HTTP_201_CREATED)
        except:
            try:
                contactus = Contactus.objects.create(**request.data)
                contactus = ContactSerializer(contactus).data
                return Response(contactus, status=status.HTTP_201_CREATED)
            except:
                return Response({"massege": "please enter the correct objects"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, contact_id):
        permission_classes = (IsAdminUser,)
        try:
            contactus = Contactus.objects.filter(id=contact_id)
            if contactus.exists():
                contactus.update(**request.data)
                contactus = Contactus.objects.get(id=contact_id)
                contactus = ContactSerializer(contactus).data
                return Response(contactus, status=status.HTTP_200_OK)

            else:
                contactus = Contactus.objects.all()
                contactus = ContactSerializer(contactus, many=True).data
                data = {
                    "massege": "id:{}, not existsed".format(contact_id),
                    "existdata": contactus
                }
                return Response(data, status=status.HTTP_409_CONFLICT)
        except:
            return Response({"massege": "please enter the correct objects"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, contact_id):
        # permission_classes = (IsAdminUser,)
        contact = Contactus.objects.filter(id=contact_id)
        if contact.count() > 0:
            contact = Contactus.objects.get(id=contact_id)
            contact.delete()
            return Response({"massege": "id: {}, deleted successfully".format(contact_id)}, status=status.HTTP_200_OK)

        else:
            contact = Contactus.objects.all()
            contact = ContactSerializer(contact, many=True).data
            data = {
                "massege": "id:{}, was not found!".format(contact_id),
                "existdata": contact
            }
            return Response(data, status=status.HTTP_409_CONFLICT)
