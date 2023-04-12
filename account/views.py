from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .signals import *
from .serializers import *
from django.db import IntegrityError


class AutheView(APIView):
    def get(self, request, user_id=None):
        if request.user.is_staff:
            user = User.objects.filter(id=user_id)
            if user.count() == 0:
                return Response({"message": "User with this profile was not found!"},
                                status=status.HTTP_400_BAD_REQUEST)
            user = Profile.objects.get(user_id=user_id)
            user = ProfileSerializer(user).data
            return Response(user, status=status.HTTP_302_FOUND)
        else:
            try:
                user = Profile.objects.get(user_id=request.user.id)
                user = ProfileSerializer(user).data
                context = {
                    "massege": "access denied",
                    "your profile": user
                }
                return Response(context, status=status.HTTP_400_BAD_REQUEST)
            except:
                return Response({"massege": "permission error"}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

    def post(self, request):
        try:
            user = User.objects.create_user(username=request.data["username"], password=request.data["password"])
            user = UserSerializer(user).data

            return Response(user, status=status.HTTP_201_CREATED)
        except IntegrityError:
            return Response({"error": "username already exists"}, status=status.HTTP_409_CONFLICT)
        except Exception as err:
            return Response({'error': str(err)}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, req):
        # permission_classes = (Authenticate,)
        user = User.objects.filter(id=req.user.id).update(**req.data)
        user = User.objects.get(id=req.user.id)
        user = UserSerializer(user).data

        return Response(user, status=status.HTTP_200_OK)

    def delete(self, request, user_id):
        if request.user.is_staff:
            userid = User.objects.filter(id=user_id)
            if userid.count() > 0:
                user = User.objects.get(id=user_id)
                user.delete()
                return Response({"message": "user {} deleted successfully".format(user_id)},
                                status=status.HTTP_200_OK)
            else:
                user = User.objects.all()
                user = UserSerializer(user, many=True).data
                data = {
                    "massege": "user id:{}, was not found!".format(user_id),
                    "existdata": user
                }
                return Response(data, status=status.HTTP_409_CONFLICT)
        else:
            return Response({"message": "access denied"}, status=status.HTTP_400_BAD_REQUEST)

class AddressView(APIView):
    def post(self, request):
        user_id = request.user.id
        address = Address.objects.create(user_id=1, **request.data)
        address = AddressSerializer(address).data
        return Response(address, status=status.HTTP_201_CREATED)