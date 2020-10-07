from django.shortcuts import render
from django.http import JsonResponse


#third party imports
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


#import models from database
from chat.models import ChatRoom
from .serializers import ChatRoomSerializer

# Create your views here.
# def index(request):
    # data = {'name': "Jorden", 'age': 23}
#     return JsonResponse(data)


class TestView(APIView):
    #built in authorization
    # permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        #getting all instances of model
        qs = ChatRoom.objects.all()
        serializer = ChatRoomSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ChatRoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


