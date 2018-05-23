from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from app1.models import Customers
import json
from django.core import serializers

# Create your views here.
def index(request):
    return TemplateResponse(request, 'index.html', {'name': 'world'})
    # return render(request, 'app1/index.html', {'name': 'world'})

def getList(request):
    r=Customers.objects.all()[:2]
    result = {
        'count': 0,
        'data': list(r.values())
    }
    data = json.dumps(result)
    print(data)
    return HttpResponse(data, content_type="application/json")
