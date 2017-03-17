from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render_to_response, get_object_or_404, render
from .models import Item
from redis import Redis
import pili
import json

redis = Redis(host='redis', port=6379)

AccessKey = "ZAhmAzHOEsDN6ecIx4JMZrtopwKGo7FLilTNVc6y"
SecretKey = "YfwFlPoiVWwsqOaUX0Uws2gUivlYW997f0Rc23tL"
HubKey = "xijinfaoutsourcing"
StreamKey = "headquarter"

def home(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')
    items = Item.objects.all()
    counter = redis.incr('counter')
    return render(request, 'home.html', {'items': items, 'counter': counter})

def streamPushList(request):

	mac = pili.Mac(AccessKey, SecretKey)

	rtmppushurl = pili.rtmp_publish_url("pili-publish.xijinfa.cn", HubKey, StreamKey, mac, 604800)

	datalist = {}
	datalist["push_url"]=rtmppushurl

	jsonblock={}
	jsonblock['errCode']=0
	jsonblock['errMsg']=""
	jsonblock['result']=datalist
	data = json.dumps(jsonblock)
	return HttpResponse(data, content_type="application/json; charset=utf-8")

def streamPlayList(request):

	mac = pili.Mac(AccessKey, SecretKey)

	rtmpplayurl = pili.rtmp_play_url("pili-live-rtmp.xijinfa.cn", HubKey, StreamKey)
	hlsplayurl = pili.hls_play_url("pili-live-hls.xijinfa.cn", HubKey, StreamKey)

	datalist = {}
	datalist["rtmp_play_url"]=rtmpplayurl
	datalist["hls_play_url"]=hlsplayurl

	jsonblock={}
	jsonblock['errCode']=0
	jsonblock['errMsg']=""
	jsonblock['result']=datalist
	data = json.dumps(jsonblock)
	return HttpResponse(data, content_type="application/json; charset=utf-8")

def streamStatus(request):
	mac = pili.Mac(AccessKey, SecretKey)
	client = pili.Client(mac)
	hub = client.hub(HubKey)
	stream = hub.get(StreamKey)
	return HttpResponse(stream.to_json(), content_type="application/json; charset=utf-8")
