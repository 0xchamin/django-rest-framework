import json

from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import View #class based views

from .models import Update
from appapi.mixins import JsonResponseMixin

# def detail_view(request):
#     #return render() #return Python Dict -
#     return HttpResponse(get_template().render({}))


##update model detail view
# def json_view_view(request):
#     #returns json dict
#     data = {
#         "count":10,
#         "name":"apple"
#     }
#     json_data = json.dumps(data)
#     #return JsonResponse(data)
#     return HttpResponse(json_data, content_type='application/json') #python way of doing it

class JsonCBV(View):
    def get(self, request, *args, **kwargs):
        data = {
            "count":10,
            "name":"apple"
        }
        return JsonResponse(data)

class JsonCBV2(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        data = {
            "count":10,
            "name":"apple"
        }
        return self.render_to_json_response(data)


#single view
class SerializedDetailViewOld(View):
    def get(self, request, *args, **kwargs):
        obj = Update.objects.get(id=1)
        data = serialize("json", [obj,],  fields=('user', 'content') )
        # data = {
        #     "user": obj.user.username,
        #     "content": obj.content
        # }
        # json_data = json.dumps(data)
        json_data = data
        return HttpResponse(json_data, content_type='application/json')

#single view
class SerializedDetailView(View):
    def get(self, request, *args, **kwargs):
        obj = Update.objects.get(id=1)
        json_data = obj.serialize()
        return HttpResponse(json_data, content_type='application/json')

#list view : all the data (query set)
class SerializedListViewOld(View):
    def get(self, request, *args, **kwargs):
        qs = Update.objects.all() #qs is query list []
        data = serialize("json", qs)# fields=('user', 'content') )
        print(data)
        json_data = data
        # data = {
        #     "user": qs.user.username,
        #     "content": qs.content
        # }
        # json_data = json.dumps(data)
        return HttpResponse(json_data, content_type='application/json')

#
class SerializedListView(View):
    def get(self, request, *args, **kwargs):
        qs = Update.objects.all() #qs is query list []
        json_data = Update.objects.all().serialize()
        return HttpResponse(json_data, content_type='application/json')
