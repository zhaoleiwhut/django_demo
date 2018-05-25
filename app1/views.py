from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from app1.models import Customers
import json
from django.forms.models import model_to_dict
from django.core import serializers


# Create your views here.
def index(request):
    return TemplateResponse(request, 'index.html', {'name': 'world'})
    # return render(request, 'app1/index.html', {'name': 'world'})


def get_list(request):
    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    data_set = Customers.objects.all()[:10]

    # filter相当于SQL中的WHERE，可设置条件过滤结果
    # data_set = Test.objects.filter(id=1)
    # 获取单个对象
    # data_set = Test.objects.get(id=1)
    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    # data_set = Customers.objects.order_by('name')[0:2]
    # 数据排序
    # data_set = Customers.objects.order_by("id")
    # 上面的方法可以连锁使用
    # data_set = Customers.objects.filter(name="runoob").order_by("id")

    data_list = list(data_set.values())
    result = {
        'count': 0,
        'data': data_list,
    }
    data = json.dumps(result)
    return HttpResponse(data, content_type="application/json")


def save(request):
    a = Customers(CompanyName='nsfocus', Address='北京')
    a.save()
    return HttpResponse(json.dumps(model_to_dict(a)), content_type="application/json")


def update(request):
    first = Customers.objects.first()
    first.CompanyName = 'Google'
    first.save()

    # 另外一种方式
    # Test.objects.filter(id=1).update(name='Google')
    # 修改所有的列
    # Test.objects.all().update(name='Google')
    return HttpResponse(json.dumps(model_to_dict(first)), content_type="application/json")


def delete(request):
    first = Customers.objects.first()
    first.delete()
    return HttpResponse(json.dumps(model_to_dict(first)), content_type="application/json")
