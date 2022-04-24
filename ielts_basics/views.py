from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import *

class UserCreationAPIView(APIView):
    """ Creation Of All Type of Users """

    def post(self, request, *args, **kwargs):
        data = request.data
        user_name = data.get('user_name')
        email = data.get('email')
        password = data.get('password')
        contact = data.get('contact')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        common_qs = CommonUser.objects.filter(mobile_number=contact)
        if common_qs.exists():
            return Response({"message": "Mobile Number alrady exists",
                             "status": 400}, status=status.HTTP_400_BAD_REQUEST)
        user_qs = User.objects.filter(email=email)
        if user_qs.exists():
            return Response({"message": "Email alrady exists",
                             "status": 400}, status=status.HTTP_400_BAD_REQUEST)
        user = User(username=user_name,
                    first_name=first_name,
                    last_name=last_name,
                    email=email)
        user.set_password(password)
        user.save(using=self._db)
        CommonUser.objects.create(mobile_number=contact)
        Student.objects.create(user_id=user.id)
        return Response({"message": "User Created Successfully",
                         "status": 201}, status=status.HTTP_201_CREATED)
