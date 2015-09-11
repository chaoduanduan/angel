from django.db import models

# Create your models here.
from django.conf import Settings

NEW_STATE = (("AL","Alabama"), ("AK","Alaska"), ("AZ","Arizona"), ("AR","Arkansas"), ("CA","California"), ("CO","Colorado"), ("CT","Connecticut"), ("DE","Delaware"), ("FL","Florida"), ("GA","Georgia"), )
        #  "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
        #  "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
        #  "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
        #  "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY")
# This is also used for user info 
class SignUp(models.Model):    
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.CharField(max_length=120)
    address2 = models.CharField(max_length=120,null = True, blank = True)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120, choices = NEW_STATE)
    country = models.CharField(max_length=120)
    zipcode = models.CharField(max_length = 10)
    phone = models.CharField(max_length = 120)
    shipping = models.BooleanField(default = True)
    billing = models.BooleanField(default = True)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
    updated = models.DateTimeField(auto_now_add = False, auto_now = True)
    def __unicode__(self):
        return self.firstName
    def get_address(self):
        return "%s, %s, %s, %s, %s"(self.address, self.city, self.state, self.country, self.zipcode)
   