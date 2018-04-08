# -*- coding: utf-8 -*-
# Imports
from django.shortcuts import get_object_or_404, render, redirect
from .models import *
# import the django settings
from django.conf import settings

# Debugging
import pdb
#pdb.set_trace()

# Create your views here.
def index(request):
    return render(request, 'main_pID/index.html')


def pIDWeb(request):
    return render(request, 'main_pID/pidweb_form.html')

