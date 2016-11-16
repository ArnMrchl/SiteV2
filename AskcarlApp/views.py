from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.views.generic import *
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def home(request):
    return render(request, 'home.html')



def blog(request):
    return render(request, 'AskcarlApp/blog.html')

def datawarehouse_registered(request):
    return render(request, 'AskcarlApp/datawarehouse_registered.html')

def datawarehouse_unregistered(request):
    return render(request, 'AskcarlApp/datawarehouse_unregistered.html')

def pricing(request):
	return render(request, 'AskcarlApp/pricing.html')


def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'AskcarlApp/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )