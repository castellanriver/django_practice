from django.shortcuts import render, HttpResponse
import random

topics = [
    {
        'id': 1,
        'title': 'routing',
        'body': 'routing is...'
    },
    {
        'id': 2,
        'title': 'view',
        'body': 'view is...'
    },
    {
        'id': 3,
        'title': 'model',
        'body': 'model is...'
    },
]

# Create your views here.


def index(request):
    global topics
    ol = ''
    for topic in topics:
        ol += f'<li>{topic["title"]}</li>'
    return HttpResponse(f'''
  <html>
  <body>
    <h1>Django</h1>
    <ol>
      {ol}
    <h2>Django</h2>
      hello django!
  </body>
  </html>

  ''')


def create(request):
    return HttpResponse('Create!')


def read(request, id):
    return HttpResponse('Read! + id')
