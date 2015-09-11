import time
from django.shortcuts import render, HttpResponseRedirect
from productions.models import Product
from django.core.urlresolvers import reverse
from .models import Order
# Create your views here.
def checkout(request): #See slug or not here later.
     
    try:
        the_id = request.session['product_id'] # id of current car        
    except:
        new_product = Product()
        new_product.save()
        request.session['product_id']=new_product.id
        the_id = new_product.id
        product = Product.objects.get(id = the_id)       
    new_order, created = Order.objects.get_or_create(product = product)
    if created:
        new_order.order_id = str(time.time())
        new_order.save()
    if new_order.status == "Finished":
        del request.session['product_id']
    context={}
    template = "prodcutions/single.html"
    return render(request, template ,context )