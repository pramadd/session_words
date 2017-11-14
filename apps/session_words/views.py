# from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
from time import gmtime, strftime


def index(request):
  # for i in request.session['inputs']:
  #     print i['word']
  #     print i['color']
  #     print i['font']
  #     print i['color']
  if 'word' not in request.session:
      request.session['word']="yyy"
  if 'color' not in request.session:
      request.session['color'] = "kkk"
  if 'font' not in request.session:
      request.session['font'] = "gg"
  if 'inputs' not in request.session:
      print "we're here"
      request.session['inputs'] = []

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
  
          temp = {
          'word':request.POST['word'],
          'color':request.POST['color'],
          'font':request.POST['font'], 
          'time':strftime("%H:%M:%S%p, %B %d, %Y", gmtime())
          }
        temp2 = request.session['inputs']
        temp2.append(temp)
        request.session['inputs'] = temp2

        # request.session['inputs'].append(temp)
        # for i in request.session['inputs']:
        #   print "yarrrr"
        #   print i['word']
        #   print i['color']
        #   print i['font']
          
        return redirect('/')

def clear(request):
  print "clearing"
  request.session['inputs'] = []
  return redirect('/')

