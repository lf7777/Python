
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Hello World!')

def search(request):
    return render(request,'search_form.html')

def search_(request):
    request.encoding='utf-8'
    content=request.POST.get('search_information')
    return HttpResponse("返回给你:"+content)
