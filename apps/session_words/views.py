from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
from time import gmtime, strftime


def index(request):
  if 'word' not in request.session:
      request.session['word']="yyy"
  if 'color' not in request.session:
      request.session['color'] = "kkk"
  if 'font' not in request.session:
      request.session['font'] = "gg"

  return render(request,'session_words/index.html')

def process(request):
        print "uuuuu"
        print request.POST
        # if request.POST['font'] == "bold":
        #   print "iiiiiiiiii"
        if request.POST["font"] == True:
          print "fghjkjhgbf"
        else:
          print "false"
          request.POST["font"] == False
   
          request.session['inputs'] = request.session['inputs']
          temp = {
          'word':request.POST['word'],
          'color':request.POST['color'],
          'font':request.POST['font'], 
          'time':strftime("%H:%M:%S%p, %B %d, %Y", gmtime())
          }
        request.session['inputs'].append(temp)
        return redirect('/')
def clear(request):
  request.session['inputs'] = []
  return redirect('/')

