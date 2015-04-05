from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpRequest
from urllib.request import urlopen
from bs4 import BeautifulSoup

def url_format(string):
    s = string.lower()
    s = s.replace(' ', '_')
    return s

def build_url(artist, title):
    artist = url_format(artist)
    title = url_format(title)
    url = 'http://www.911tabs.com/tabs'
    url += '/' + artist[0]
    url += '/' + artist
    url += '/' + title
    url += '_tab.htm'
    return url

def get_tabs(artist, title):
    print(artist)
    print(title)

    url = build_url(artist, title)
    print(url)

    response = urlopen(url)
    print(response)

    soup = BeautifulSoup(response).read()
    print(soup)

    songs_ele = None
    tabs = []
    for article in soup.find_all('article'):
        if 'b-table_song' in article['class']: songs_ele = article
    for a in songs_ele.find_all('a'):
        tabs.append(a['data-url'])
    return tabs

def home(request):
    context = {}
    if request.method == 'GET':
        template = 'form.html'
    if request.method == 'POST':
        template = 'results.html'
        artist =  request.POST['artist']
        title = request.POST['title']
        context = {'tabs': get_tabs(artist, title)}
    return render_to_response(template, RequestContext(request, context))

