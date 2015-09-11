from django.db import models
from productions.models import CarInfo
# Create your models here.
STATUS_CHOICES = (
    ("Started","Started"),
    ("Abondoned","Abondoned"),
    ("Finished","Finished"),    
)
class Order(models.Model):
    carselected = models.ForeignKey(CarInfo)
    status = models.CharField(max_length = 120, choices= STATUS_CHOICES,default = "Started")
    order_id = models.CharField(max_length = 120, default = 'ABC', unique = True)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
    updated = models.DateTimeField(auto_now_add = False, auto_now = True)
    
    def __unicode__(self):
        return self.order_id