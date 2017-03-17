from django.shortcuts import render
import json
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import urllib2, urllib, httplib
import socket
import sys
import os
from HTMLParser import HTMLParser
from HTMLParser import HTMLParseError
import time
from .models import Topic, Item, ItemData, Content

# Create your views here.

def topic(request):
	topic_list = Topic.objects.filter(is_valid=True)
	data = serializers.serialize("json", topic_list)
	return HttpResponse(data, content_type="application/json; charset=utf-8")

def subtopic(request, topic_id):
    item_list = []
    if topic_id > 0:
        try:
            topic = Topic.objects.get(id=topic_id)
            item_list = Item.objects.filter(topic = topic, is_valid=True)
        except Topic.DoesNotExist:
            pass
    data = serializers.serialize("json", item_list)
    return HttpResponse(data, content_type="application/json; charset=utf-8")

def item(request):
	item_list = Item.objects.filter(is_valid=True)
	data = serializers.serialize("json", item_list)
	return HttpResponse(data, content_type="application/json; charset=utf-8")

def post(request):
    itempage = request.GET.get('page', 1)
    pagesize = request.GET.get('pagesize', 20)
    itempage = int(itempage)
    pagesize = int(pagesize)
    if itempage > 0:
        beginnum = pagesize * (itempage - 1)
        endnum = pagesize * itempage
        content_list = ItemData.objects.all().order_by('-postdate')[beginnum:endnum]

        data = serializers.serialize("json", content_list)
        return HttpResponse(data, content_type ="application/json; charset=utf-8")
    return HttpResponse(itempage, content_type ="text/plain; charset=utf-8")

def content(request):
    contenturl = request.GET.get('link', 1)
    contenturl = str(contenturl)
    if len(contenturl) > 0:
        content_list = Content.objects.filter(rootlink=contenturl)
        data = serializers.serialize("json", content_list)
        return HttpResponse(data, content_type="text/plain; charset=utf-8")
    else:
        return HttpResponse("fail", content_type="text/plain; charset=utf-8")

def contentExist(request):
    contenturl = request.GET.get('link', 1)
    contenturl = str(contenturl)
    if len(contenturl) > 0:
        try:
            Content.objects.get(rootlink = contenturl)
            return HttpResponse("ok", mimetype="text/plain; charset=utf-8")
        except Content.DoesNotExist:
            return HttpResponse("fail", mimetype="text/plain; charset=utf-8")
    else:
        return HttpResponse("fail", mimetype="text/plain; charset=utf-8")

@csrf_exempt
def updateContent(request):
    if request.method == 'POST':
        link = request.POST.get('link')
        content = request.POST.get('content')
        try:
            datacontent = Content.objects.get(rootlink = link)
            datacontent.content = content
            datacontent.save()
        except Content.DoesNotExist:
            Content.objects.create(rootlink = link, content = content)

        return HttpResponse(link+content, content_type="text/plain; charset=utf-8")
    return HttpResponse('[ok]', content_type="text/plain; charset=utf-8")

@csrf_exempt
def updatas(request):
    #get raw post data  and parse json.
    #print request.method
    if request.method == 'POST':
        pk = request.POST.get('pk')
        data = request.POST.get('list')
        jsondata = json.loads(data, encoding='utf-8')
        #print type(data)
        #print type(jsondata)
        #print jsondata
        for i in range(len(jsondata)):
            link = jsondata[i][1]
            try:
                ItemData.objects.get(item_id = pk, link = link)
                print 'exist'
            except ItemData.DoesNotExist:
                i = ItemData.objects.create(item_id = pk, name = jsondata[i][0], link = jsondata[i][1], imageurl = jsondata[i][2], content = jsondata[i][3], postdate = jsondata[i][4], is_valid=True)
                i.save()
                print 'added'
        return HttpResponse("[post ok]", content_type="text/plain; charset=utf-8")
    return HttpResponse('[ok]', content_type="text/plain; charset=utf-8")



