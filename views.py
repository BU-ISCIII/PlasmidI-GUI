# -*- coding: utf-8 -*-
# Imports
import json
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import *
# import the django settings
from django.conf import settings

from django.views.generic import CreateView, DeleteView, ListView
from .response import JSONResponse, response_mimetype
from .serialize import serialize

# Debugging
import pdb
#pdb.set_trace()

# Create your views here.
def index(request):
    return render(request, 'main_pID/index.html')


# def pIDWeb(request):
#     return render(request, 'main_pID/pidweb_form.html')

class pIDWebView(CreateView):
    model = Jobs
    fields = ('file_R1','file_R2',)
    exclude = ['job_id',]
    template_name = "main_pID/pidweb_form2.html"

    def form_valid(self, form):
        self.object = form.save()
        file_R1 = [serialize(self.object,file_attr="file_R1")]
        file_R2 = [serialize(self.object,file_attr="file_R2")]

        data = {'files': file_R1 + file_R2}
        response = JSONResponse(data, mimetype=response_mimetype(self.request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response

    def form_invalid(self, form):
        data = json.dumps(form.errors)
        #pdb.set_trace()
        return HttpResponse(content=data, status=400, content_type='application/json')

class FileDeleteView(DeleteView):
    model = Jobs
    template_name = "main_pID/pidweb_form2.html"

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        response = JSONResponse(True, mimetype=response_mimetype(request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response

# class FileListView(ListView):
#     model = Jobs
#     template_name = "main_pID/pidweb_form2.html"
# #
#     def render_to_response(self, context, **response_kwargs):
#         file_R1 = [ serialize(p,file_attr="file_R1") for p in self.get_queryset() ]
#         file_R2 = [ serialize(p,file_attr="file_R2") for p in self.get_queryset() ]
#         files = file_R1 + file_R2
#         #pdb.set_trace()
#         data = {'files':files}
#         response = JSONResponse(data, mimetype=response_mimetype(self.request))
#         response['Content-Disposition'] = 'inline; filename=files.json'
#         return response
