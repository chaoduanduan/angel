from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:$ means string is done
    url(r'^$', 'productions.views.home', name='home'),
    url(r'^signup/$','signups.views.registration', name ='registration'),
    url(r'^upload/$','productions.views.upload', name='upload'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^carinfo/$','productions.views.carinfo', name ='carinfo'),
    url(r'^car/s/$','productions.views.search', name ='search'),
    url(r'^carinfo/(?P<slug>[\w-]+)/$','productions.views.single', name ='single_product'),
    url(r'^checkout/$','orders.views.checkout', name = 'checkout'),
    url(r'^login/$','signups.views.login',name = 'login'),
    # url(r'^blog/',include('blog.urls')),
    #(?P<all_items>.*)
    #(?P<id>\d+)
    url(r'^cars/s/$','productions.views.dropdownsearch', name ='dropdownsearch'),
    url(r'^cars/$','productions.views.cars',name = 'cars'),
    
    url(r'^upload/uploadsuccess/$','productions.views.uploadsuccess', name ='uploadsuccess'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^form/$','productions.views.Form', name = 'form'),
    url(r'^imageupload/$','productions.views.imageupload', name = 'imageupload'),
    url(r'^cars/(?P<slug>[\w-]+)/$','productions.views.detail', name = 'detail'),
    url(r'^accounts/',include('registration.backends.default.urls')),
    url(r'^cart/$','carts.views.view',name = 'cart'),
    url(r'^cart/(?P<slug>[\w-]+)/$','carts.views.update_cart', name ='update_cart'),
    url(r'^cart/(?P<id>\d+)/$','carts.views.remove_from_cart', name ='remove_from_cart'),
    
    url(r'^contact/$','productions.views.contact', name ='contact'),
) #+ static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)