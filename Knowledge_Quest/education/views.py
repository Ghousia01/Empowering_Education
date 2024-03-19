
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Resource
from django.template import loader
from .forms import Feedbackform
from django.contrib import messages


# Create your views here.
def welcome_page(request):
    return render(request, 'education/welcome.html')

def index(request):
    resource_list = Resource.objects.all()
    template = loader.get_template('education/index.html')
    context ={
        'resource_list':resource_list,
    }
    return render(request,'education/index.html',context)


def detail(request,resource_id):
    resource = Resource.objects.get(pk = resource_id)
    context ={
        'resource':resource,
    }
    return render(request, 'education/detail.html', context)

def add_feedback(request): 
    form = Feedbackform(request.POST or None) 
 
    if form.is_valid():
        form.save() 
        return redirect('education:index') 
    return render(request, 'education/feedback_form.html', {'form':form}) 




