from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    colors = ['#FFA46B','#FF6A59', '#ED2853', '#6B5D4E']
    adv = ['disgustingly', 'uniquely', 'slightly', 'frighteningly', 'blatantly']
    adj = ['awesome', 'legit', 'shitty', 'awful', 'METAL']
    html = '<!doctype html><html><head><title>Alex is so&hellip;</title>'                                                                                                                                         
    html += "<link href='http://fonts.googleapis.com/css?family=Sigmar+One' rel='stylesheet' type='text/css'>"
    html += '<style>'
    html += 'html,body { background: ' + random.choice(colors) + '; height: 100%; }'
    html += 'h1 { width: 70%; margin: auto; text-shadow: 3px 3px rgba(0,0,0,0.3); color: #F7E494; font: 80px/1.3 "Sigmar One", sans-serif; position: relative; top: 50%; -webkit-transform: translateY(-50%); -ms-transform: translateY(-50%); transform: translateY(-50%); }'
    html += '</style></head></body>'
    html += '<h1>Alex is so ' + random.choice(adv) + ' ' + random.choice(adj) + '.</h1>'
    html += '</body></html>'
    return HttpResponse(html)

