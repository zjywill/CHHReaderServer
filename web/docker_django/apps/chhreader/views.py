from django.shortcuts import render
import json
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
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
from .models import Topic, ItemData, Content


# Create your views here.

def topics(request):
    topic_list = Topic.objects.filter(is_valid=True)
    if len(topic_list) == 0:
        return HttpResponseNotFound()
    data_list = []
    for topic_data in topic_list:
        topic_item = {}
        topic_item['id'] = topic_data.id
        topic_item['name'] = topic_data.name
        topic_item['source_link'] = topic_data.source_link
        data_list.append(topic_item)
    data = json.dumps(data_list)
    return HttpResponse(data, content_type="application/json; charset=utf-8")


@csrf_exempt
def articles(request):
    if request.method == 'GET':
        return get_articles(request)
    elif request.method == 'POST':
        return post_articles(request)
    else:
        return HttpResponseNotFound()


def get_articles(request):
    itempage = request.GET.get('page', 1)
    pagesize = request.GET.get('pagesize', 20)
    itempage = int(itempage)
    pagesize = int(pagesize)
    if itempage > 0:
        beginnum = pagesize * (itempage - 1)
        endnum = pagesize * itempage
        content_list = ItemData.objects.all().order_by('-postdate')[beginnum:endnum]
        if len(content_list) == 0:
            return HttpResponseNotFound()
        data_list = []
        for article_data in content_list:
            article_item = {}
            article_item['id'] = article_data.id
            article_item['name'] = article_data.name
            article_item['topic'] = article_data.topic.name
            article_item['link'] = article_data.link
            article_item['image_url'] = article_data.image_url
            article_item['content'] = article_data.content
            article_item['postdate'] = article_data.postdate
            data_list.append(article_item)
        data = json.dumps(data_list)
        return HttpResponse(data, content_type="application/json; charset=utf-8")
    return HttpResponseNotFound()


def post_articles(request):
    topic_id = request.POST.get('topic_id')
    data = request.POST.get('list')
    jsondata = json.loads(data, encoding='utf-8')
    # print type(data)
    # print type(jsondata)
    # print jsondata
    for i in range(len(jsondata)):
        link = jsondata[i][1]
        try:
            ItemData.objects.get(link=link)
            print 'exist'
        except ItemData.DoesNotExist:
            i = ItemData.objects.create(topic_id=topic_id, name=jsondata[i][0], link=jsondata[i][1],
                                        image_url=jsondata[i][2], content=jsondata[i][3], postdate=jsondata[i][4],
                                        is_valid=True)
            i.save()
            print 'added'
    return HttpResponse("[post ok]", content_type="text/plain; charset=utf-8")


@csrf_exempt
def content(request):
    if request.method == 'POST':
        root_link = request.POST.get('link')
        content_detail = request.POST.get('content')
        try:
            item = ItemData.objects.get(link=root_link)
            updateContent(root_link, content_detail)
        except ItemData.DoesNotExist:
            return HttpResponseNotFound()
        return HttpResponse("[ok]", content_type="text/plain; charset=utf-8")
    else:
        return HttpResponseNotFound()


def viewContent(request, query_id):
    if request.method == 'GET':
        query_link = ""
        try:
            item = ItemData.objects.get(id=query_id)
            query_link = item.link
        except ItemData.DoesNotExist:
            return HttpResponseNotFound()
        try:
            content_data = Content.objects.get(root_link=query_link)
            contentItem = {}
            contentItem['link'] = content_data.root_link
            contentItem['content'] = content_data.content
            data = json.dumps(contentItem)
            return HttpResponse(data, content_type="application/json; charset=utf-8")
        except Content.DoesNotExist:
            return HttpResponseNotFound()
    else:
        return HttpResponseNotFound()


def updateContent(link, content):
    try:
        dataContent = Content.objects.get(root_link=link)
        dataContent.content = content
        dataContent.save()
    except Content.DoesNotExist:
        Content.objects.create(root_link=link, content=content)
