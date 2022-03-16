from django.shortcuts import render
from rest_framework import generics, status
from .models import Room
from .serializers import RoomSerializer, CreateRoomSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class RoomView(generics.ListAPIView): 
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    
class GetRoom(APIView): 
    serializer_class = RoomSerializer
    lookup_url_kwarg = 'code'
    
    def get(self, request, format=None): 
        code = request.GET.get(self.lookup_url_kwarg)
        if code != None: 
            room = Room.objects.filter(code=code)
            #if there is a room that matches the code get the data from the serializer
            if len(room) > 0: 
                data = RoomSerializer(room[0]).data
                data['is_host'] = self.request.session.session_key == room[0].host
                return Response(data, status=status.HTTP_200_OK)
            return Response({'Room Not Found': 'Invalid Room Code'}, status=status.HTTP_404_NOT_FOUND)
        
        return Response({'Bad Request': 'Code parameter not found in request'}, status=status.HTTP_400_BAD_REQUEST)


class CreateRoomView(APIView): 
    serializer_class = CreateRoomSerializer
    
    def post(self, request, format=None):
        #checking if person has a session key
        if not self.request.session.exists(self.request.session.session_key): 
            self.request.session.create()
        
        #checking if the request is valid meaning it has the required data points that we said a request must have
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(): 
            #get data for request from serializer
            guest_can_pause = serializer.data.get('guest_can_pause')
            votes_to_skip = serializer.data.get('votes_to_skip')
            host = self.request.session.session_key
            #check if a there already exists a room tied to that session key (host)
            queryset = Room.objects.filter(host=host)
            if queryset.exists():
                #if yes update the room setting to match the new request
                room = queryset[0]
                room.guest_can_pause = guest_can_pause
                room.votes_to_skip = votes_to_skip
                #after making the changes must do following so it actually gets updated
                room.save(update_fields=['guest_can_pause', 'votes_to_skip'])
                #serialize the new room or updated room using the room serializer
                #.data will give us json format
                return Response(RoomSerializer(room).data, status=status.HTTP_200_OK)
            else: 
                #if not create a new room for that host
                room = Room(host=host, guest_can_pause=guest_can_pause, votes_to_skip=votes_to_skip)
                room.save()
                #serialize the new room or updated room using the room serializer
                #.data will give us json format
                return Response(RoomSerializer(room).data, status=status.HTTP_201_CREATED)
            
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)
            