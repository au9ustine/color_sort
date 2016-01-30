from __future__ import print_function
from django.shortcuts import render
import urllib
import cStringIO
from PIL import Image
from calc import *
import json
import math
# Create your views here.

def index(request):
    keys = ['_'.join([i, 'sq320']) for i in get_keys('http://api.huaban.com/explore/yanchuhaibao/')]
    ctx = []
    for k in keys:
        remote_path = ''.join(["http://img.hb.aicdn.com/", k])
        local_path = ''.join(['colour_sort/static/', k])
        urllib.urlretrieve(remote_path, local_path)
        c = CalcRGBAvg(local_path)
        ctx.append((''.join(['/static/',k]), c.calculate(get_luminance_val)))
    ctx.sort(key=lambda x:x[1])

    return render(request, 'portal.html', {'img_urls': ctx})

def get_keys(group_url):
    json_obj = json.loads(urllib.urlopen(group_url).read())
    for i in json_obj['explores']:
        yield i['cover']['key']
