from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')
def submitquery(request):
    q=request.GET['query']
    try:
        ans=eval(q)
        mydictionary={
        "q":q,
        "ans":ans,
        "error":False
    }        
        return render(request,"index.html",context=mydictionary)
    except:
          mydictionary={
               "error":True
          }
          return render(request,"index.html",context=mydictionary)
          #return HttpResponse(q)