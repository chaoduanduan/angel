from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Cart
from productions.models import CarInfo
def view(request):
    try:
        the_id = request.session['cart_id']     
    except:
        the_id= None
    if the_id:
        cart = Cart.objects.get(id = the_id)
        context = {"cart":cart}
    else:
        empty_message="Your Cart is Empty, Add Something Here."
        context = {"empty": True,"empty_message": empty_message}
    template = "carts/view.html"
    return render(request,template,context)
def remove_from_cart(request,id):
    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id = the_id)
    except:
        return HttpResponseRedirect(reverse('cart'))
    caritem = cart.products.get(id=the_id)    
    caritem.delete()
    cartitem = None
    cart.save()
    return HttpResponseRedirect(reverse('cart'))
        

def update_cart(request,slug):
    request.session.set_expiry(30000)
    # After 300 seconds, the session times out.The cart turns inactive
    # To see if there is a session id for cart. if not, then create one
    # Try cart first
    try:
        the_id=request.session['cart_id']
       #if no cart_id, then creat one cart.
    except:
        new_cart= Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id
    cart = Cart.objects.get(id=the_id)
    # Then Product Information
    try:
        carinfo = CarInfo.objects.get(slug = slug)
        if not carinfo in cart.products.all():
            cart.products.add(carinfo)
        else:
            cart.products.remove(carinfo)
    except CarInfo.DoesNotExist:
        pass 
    
    
   
    new_total=0.00
    for item in cart.products.all():
        new_total += float(item.price)
    request.session['items_total']=cart.products.count()
    cart.total = new_total
    # Haven't used total price yet. Reserved here.
    cart.save()
    
    return HttpResponseRedirect(reverse("cart"))