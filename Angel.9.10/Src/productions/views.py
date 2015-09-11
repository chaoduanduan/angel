from django.shortcuts import render,Http404 , render_to_response, redirect, RequestContext
from django.http import HttpResponse
from django.db import models
from .models import Product,CarModel,CarInfo
from .forms import UploadForm,ImageForm,CarImageUploadForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.forms.formsets import formset_factory
import smtplib, os
from django.conf import settings
from django import forms
from crispy_forms.helper import FormHelper
from carts.models import Cart
from django.core import serializers
# Create your views here.
def carinfo(request):
    # authentication here is used for admin change here later
    products = Product.objects.all()
    context = {"products":products}
    # "products" is used for html to call context   
    template = 'productions/carinfo.html'
    return render(request,template,context)

def search(request):
    try:
        q = request.GET.get('q')
    except:
        q = None
    if q:
        products = CarInfo.objects.filter(model__icontains = q)
        context = {'query':q,'products':products}
        template ='productions/results.html'
    else:
        template = 'prodcutions/cars.html'
        context = {}
    return render(request,template,context)
   
def home(request):
    template = 'index.html'
    context = {"username_is":"aaaa"}
    return render(request,template,context)

def single(request,slug):   
    try:        
        product = Product.objects.get(slug=slug)         
        context = {"product":product}
        # "products" is used for html to call context       
        template = 'productions/single.html'
        return render(request,template,context)
    except:
        raise Http404
# Multiple images to upload!!!!!!!!!!!!!!!!!!!
#def upload(request):  
#    form = UploadForm(request.POST or None)    
 #   if form.is_valid():
 #       save_it = form.save(commit = False)
 #       save_it.save()
 #       return redirect("/upload/uploadsuccess/")
 #   else: 
 #       return render_to_response("productions/upload.html",locals(),context_instance = RequestContext(request))
#TODO: fixed the html
def uploadsuccess(request):
    template = 'productions/uploadsuccess.html'
    context={}
    return render(request,template,context)
def cars(request):
    doubledroplst=[]
    doubledownlst =[]
    is_have  = False
    
     #Pagination
    allproducts = CarInfo.objects.all()
    paginator = Paginator(allproducts,8)# show 5 cars in one page
    page = request.GET.get('page')
    try:
        cars = paginator.page(page)
    except PageNotAnInteger:
        cars = paginator.page(1)
    except EmptyPage:
        cars = paginator.page(paginator.num_pages)
    #end of Pagination
    
    modelinfos = CarModel.objects.all()
    for p in modelinfos:
        #print(p.make)
        for f in doubledroplst:
            if "%s"%(p.make) ==f:
                is_have = True
        if  is_have == False:
            doubledroplst.append("%s"%(p.make))
        is_have = False

    
    
    for p in modelinfos:
        doubledownlst.append(["%s"%(p.make),"%s"%(p.model)])
  #  js_data = simplejson.dumps(doubledroplst)  
   
    
   
    carmodel = CarModel.objects.filter(model__contains=allproducts.model)
    context = {"cars":cars,"carmodel":carmodel,"modelinfos":modelinfos, " doubledroplst": doubledroplst, "doubledownlst":doubledownlst}
    template = 'productions/cars.html'
    return render_to_response(template,locals(), context_instance = RequestContext(request))
# dropdownsearch only needs to pass the value of car model to find the exact car and if possible we need the time to find the used car information.
# TODO: add years to filter.
def dropdownsearch(request):
    doubledroplst=[]
    doubledownlst =[]
    is_have  = False
    
     #Pagination
    allproducts = CarInfo.objects.all()
    paginator = Paginator(allproducts,4)# show 5 cars in one page
    page = request.GET.get('page')
    try:
        cars = paginator.page(page)
    except PageNotAnInteger:
        cars = paginator.page(1)
    except EmptyPage:
        cars = paginator.page(paginator.num_pages)
    #end of Pagination
    
    modelinfos = CarModel.objects.all()
    for p in modelinfos:
        #print(p.make)
        for f in doubledroplst:
            if "%s"%(p.make) ==f:
                is_have = True
        if  is_have == False:
            doubledroplst.append("%s"%(p.make))
        is_have = False

    carmodel = CarModel.objects.filter(model__contains=allproducts.model)
    
    for p in modelinfos:
        doubledownlst.append(["%s"%(p.make),"%s"%(p.model)])
   # js_data = simplejson.dumps(doubledroplst)
    
    try:        
        q = request.GET.get('q')
        x = request.GET.get('x')
        y = request.GET.get('y')
        p = request.GET.get('p')
        priceup = request.GET.get('priceup')
        pricedown = request.GET.get('pricedown')
    except:
   
       q = None
       x = None
       y = None
       p = None
      
    if q or x or y or p:
        allcars = CarInfo.objects.all()
        modelinfos = CarModel.objects.all()
        if not x:
            x = 0
        if not y:
            y = 999999
        if not q:
            q = "a"
        if not priceup:
            priceup = 9999999999
        if not pricedown:
            pricedown = 0
        if p == "All":
            cars_m = CarInfo.objects.filter(mileage__range =  (x, y))
            cars = cars_m.filter(price__range =  (pricedown, priceup))
        elif q == "All":
            car_make = CarInfo.objects.filter(model__make__contains = p)
            cars = car_make.filter(mileage__range =  (x, y))
            cars = cars.filter(price__range =  (pricedown, priceup))
        else:  
            car_mod = CarInfo.objects.filter(model__model__contains = q)
            cars= car_mod.filter(mileage__range = (x, y))
            cars = cars.filter(price__range =  (pricedown, priceup))
        template ='productions/resultstwo.html'
        context = {"cars":cars,"carmodel":carmodel,"modelinfos":modelinfos, " doubledroplst": doubledroplst,"doubledownlst":doubledownlst}
    else:
        template = 'prodcutions/cars.html'
        context = {}
        
    return render_to_response(template,locals(),context_instance = RequestContext(request))

def Form(request):
    return render(request,"productions/form.html",{})
def imageupload(request):
    for count, x in enumerate(request.FILES.getlist("files")):
        def process(f):
            with open('prodcutions/images/' + str(count),'wb+') as destination:
                for chunk in f.chunks():
                    detination.write(chunk)
        process(x)
    return HttpResponse("File(s) uploaded!")
def detail(request,slug):
    try:        
        carinfo = CarInfo.objects.get(slug=slug)
        existed = False
        context = {"carinfo":carinfo,"existed":existed}
        # "products" is used for html to call context       
        template = 'productions/detail.html'
        return render(request,template,context)
    except:
        raise Http404        
def upload(request):
   # if not request.user.is_authenticated():
    #    return redirect ("login/")
    form = UploadForm(request.POST or None)
  
    if form.is_valid():
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        vin_number = form.cleaned_data.get("vin_number")
        model = form.cleaned_data.get("model")
        mileage = form.cleaned_data.get("mileage")
        last_name = form.cleaned_data.get("last_name")
        first_name = form.cleaned_data.get("first_name")
        address = form.cleaned_data.get("address")
        phone_number=form.cleaned_data.get("phone_number")        
        YourEmail = "duancwd@gmail.com"
        subject = 'ANGEL TECH AUTO SERVICES'
        from_email = settings.EMAIL_HOST_USER      
        to_email  = [settings.EMAIL_HOST_USER,YourEmail]
        contact_message = "Dear Mr  model: !!" 
        send_mail(subject,
                 contact_message,
                 from_email,
                 to_email,
                 fail_silently = True,)      
            
        save_it = form.save(commit = False)        
        save_it.save()
        return redirect("/upload/uploadsuccess/")
    else:
        return render_to_response("productions/upload.html",locals(),context_instance = RequestContext(request))
def contact(request):
    template = 'contact.html'
    context={}
    return render(request,template,locals())