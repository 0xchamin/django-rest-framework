import json

from django.views.generic import View
from django.http import HttpResponse
from updates.models import Update as UpdateModel
from updates.forms import UpdateModelForm

from appapi.mixins import HttpResponseMixin
from .mixins import CSRFExemptMixin

class UpdateModelDetailAPIView(HttpResponseMixin, CSRFExemptMixin, View):

    is_json = True

    def get(self, request, id, *args, **kwargs):
        obj = UpdateModel.objects.get(id=id)
        json_data = obj.serialize();
        return self.render_to_response(json_data)

    def post(self, request, *args, **kwargs):
        json_data= json.dumps({"message": "Not alllowed, please use correct endpoint"})
        return self.render_to_response(json_data, status=403)

    def put(self, request, *args, **kwargs):
        json_data={}
        return self.render_to_response(json_data)

    def delete(self, request, *args, **kwargs):
        json_data={}
        return self.render_to_response(json_data, status=4030)



class UpdateModelListAPIView(HttpResponseMixin, CSRFExemptMixin, View):

    is_json = True

    def get(self, request, *args, **kwargs):
        qs = UpdateModel.objects.all()
        json_data = qs.serialize()
        return self.render_to_response(json_data)

    def post(self, request, *args, **kwargs):
        print(request.POST)
        form = UpdateModelForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = obj.serialize()
            return self.render_to_response(obj_data, status=201)
        if form.errors:
            data = json.dumps(form.errors) #json.dumps({"message": "Unknown data"})
            return self.render_to_response(data, status=400)

        data = {"Message": "Method not allowed !"}
    #return HttpResponse({data}, content_type='application/json', status=201)
        return self.render_to_response(data, status=400)

    def delete(self, request, *args, **kwargs):
        data = json.dumps({"message": "You cannot delete entire list "})
        return self.render_to_response(data, status=403)
