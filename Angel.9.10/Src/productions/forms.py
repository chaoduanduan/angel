from django import forms
from .models import Product,ProductImage,CarInfo,CarModel
from django.forms.formsets import formset_factory
from crispy_forms.helper import FormHelper
class UploadForm(forms.ModelForm):
    class Meta:
        model = Product  
        
class CarImageUploadForm(forms.Form):
    class Meta:
        model = CarInfo
class ImageForm(forms.Form):
    class Meta:
        model = ProductImage
    #code
