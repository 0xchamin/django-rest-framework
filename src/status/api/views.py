#from django.views.generic import View
from rest_framework import generics, mixins
#from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from status.models import Status
from .serializer import StatusSerializer

"""
Universal one end point 
"""
class StatusAPIView(mixins.CreateModelMixin ,generics.ListAPIView): #Create List
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    ## perform search
    def get_queryset(self):
        qs = Status.objects.all()
        query = self.request.GET.get('q')

        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

        ##create model mixin
    #def perform_create(self, serializer):
    #    serializer.save(user=self.request.user)




class StatusListSearchAPIView(APIView):
    permission_classes = []
    authentication_classes = []

    #http GET
    def get(self, request, format=None):
        qs = Status.objects.all()
        serializer = StatusSerializer(qs, many=True)
        return Response(serializer.data)

    #http post
    def post(self, request, format=None):
        qs = Status.objects.all()
        serializer = StatusSerializer(qs, many=True)
        return Response(serializer.data)

#createmodelmixin --> POST data
#updatemodelmixin --> PUT data
#destroymodelmixin --> DELETE method
class StatusAPIView(mixins.CreateModelMixin ,generics.ListAPIView): #Create List
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    ## perform search
    def get_queryset(self):
        qs = Status.objects.all()
        query = self.request.GET.get('q')

        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

        ##create model mixin
    #def perform_create(self, serializer):
    #    serializer.save(user=self.request.user)

"""
Replaced with StatusAPIView
"""
# class StatusCreateAPIView(generics.CreateAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
    #

class StatusDetailAPIView(mixins.DestroyModelMixin ,mixins.UpdateModelMixin ,generics.RetrieveAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    #lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.upate(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

"""
BOTH StatusDetailAPIView AND StatusDetailAPIView are equivalent
"""

# RetrieveUpdateDestroyAPIView
class StatusDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    #lookup_field = 'id'



"""
Replaced with StatusDetailAPIView
"""
# class StatusUpdateAPIView(generics.UpdateAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#
# class StatusDeleteAPIView(generics.DestroyAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
