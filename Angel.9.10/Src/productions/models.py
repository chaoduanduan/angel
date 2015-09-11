from django.db import models
from django.core.urlresolvers import reverse
from django import forms
# Create your models here.
class Product(models.Model):
    make = models.CharField(max_length = 60)
    year = models.CharField(max_length=4)
    vin_number = models.CharField(max_length = 17,unique = True,blank = True, null = True)
    mileage = models.CharField(max_length=10)    
    phone_number = models.CharField(max_length=11)
    last_name = models.CharField(max_length = 60)
    first_name = models.CharField(max_length =60)
    email = models.EmailField() 
    address = models.CharField(max_length = 120)
    city = models.CharField(max_length =60)
    state = models.CharField(max_length=60)
    country = models.CharField(max_length=60)
    zipcode = models.CharField(max_length=5) 
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
    updated = models.DateTimeField(auto_now_add = False, auto_now = True) 
    
    def __unicode__(self):
        return self.model
  # def get_absolute_url(self):
  #      return "/carinfo/%s" %(self.slug)
  #  def get_absolute_url(self):
 #     return reverse("single_product",kwargs={"slug":self.slug})
    #kwargs : keyword arguements
    # combine carName and slug to make slug and name unique
 #   class Meta:
 #       unique_together = ('carName','slug')
 #   def get_price(self):
  #      return self.price
    # To have multiple images, then create ProductImage class
class ProductImage(models.Model):
    product = models.ForeignKey(Product)
    image = models.ImageField(upload_to= 'productions/images/')
    featured = models.BooleanField(default=False)
    thumbnail = models.BooleanField(default=False)
    def __unicode__(self):
        return self.product.model

class CarModel(models.Model):
    model = models.CharField(max_length = 60)
 #   MAKE_CHOICES = (        
 #       ('Acura','Acura'),
 #       ('Alfa Romeo','Alfa Romeo'),
 #       ('Arrinera','Artega'),
 #       ('Ascari','Ascari'),
 #       ('Aston Martin','Aston Martin'),
 #       ('Audi','Audi'),     
 #       ('BMW','BMW'),
 #       ('Bently','Bently'),
 #       ('Buick','Buick'),
 #       ('Others','Others'),  
        
  #  )
 #   make = models.CharField(max_length= 60, choices = MAKE_CHOICES, default = 'BMW')
    make = models.CharField(max_length= 60)
    year = models.IntegerField()
    cylinder_and_Rotors=models.IntegerField(null=True,blank=True)
    liter = models.DecimalField(max_digits = 20,decimal_places = 4)
    BODY_STYLE_CHOICES = (
        ("Convertible","Convertible"),
        ("Coupe","Coupe"),
        ("Full Size Van","Full Size Van"),
        ("Hatchback","Hatchback"),
        ("Minivan","Minivan"),
        ("Pickup Truck","Pickup Truck"),
        ("SUV","SUV"),
        ("Sedan","Sedan"),
        ("Sports Car","Sports Car"),
        ("Wagon","Wagon"),        
        ("Others","Others"),
    )
    FUEL_TYPE_CHOICES = (
        ("Gas","Gas"),
        ("Hybrid","Hybrid"),
        ("Electric","Electric"),
        ("Diesel","Diesel"),        
    )
    body_Style = models.CharField(max_length = 60, choices = BODY_STYLE_CHOICES, default = "SUV")
    fuel_Type = models.CharField(max_length = 60, choices = FUEL_TYPE_CHOICES, default = "Gas",null= True, blank = True)    
    horsepower = models.IntegerField()
    transmission = models.CharField(max_length = 120)
    gears = models.IntegerField(default=6)
    DRIVETRAIN_CHOICES=(
        ("Front-Wheel","Front-Wheel"),
        ("All-Wheel","All-Wheel"),
        ("Rear-Wheel","Rear-Wheel"),        
    )
    drivetrain = models.CharField(max_length =120, choices = DRIVETRAIN_CHOICES, default ="Front-Wheel")
    engine = models.CharField(max_length=120,null = True, blank = True)
    DOOR_NUMBER = (
        ("5","5"),
        ("4","4"),
        ("3","3"),
        ("2","2"),
        ("1","1"),
    )
    doors = models.CharField(max_length = 10, choices =DOOR_NUMBER, default = "4",null =True, blank =True)
    weights = models.IntegerField()
    mPG = models.IntegerField()
    additional = models.TextField(null=True,blank= True)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
    updated = models.DateTimeField(auto_now_add = False, auto_now = True)
    def __unicode__(self):
        return self.model
class CarInfo(models.Model):
    vin_number = models.CharField(max_length = 17,unique = True)
    model = models.ForeignKey(CarModel)
    price = models.DecimalField(decimal_places = 2,max_digits = 10, default = 8000.00)
    dealer = models.CharField(max_length=120,null=True, blank=True)
    Red = 'Red' # Exterior
    Blue = 'Blue'       
    Black = 'Black'
    White = 'White'
    Yellow = 'Yellow'
    Siver = 'Silver'
    Green = 'Green' #Exterior Color
    Other = 'Other'
    Beige = 'Beige' # interior Color
    Brown = 'Brown' #interior Color
    Gray ='Gray'        
    INTERIOR_COLOR_CHOICES = (
        (Red,"Red"),
        (Blue,"Blue"),            
        (Black,"Black"),
        (White,"White"),
        (Beige, "Beige"),
        (Brown,"Brown"),
        (Gray,"Gray"),
        (Other,"Other"),
    )
    EXTERIOR_COLOR_CHOICES =(           
        (Black,"Black"),
        (Blue,"Blue"),
        (Green,"Green"),
        (Red,"Red"),
        (Siver,"Silver"),
        (Yellow,"Yellow"),            
        (White,"White"),            
        (Other,"Other"),            
    )
    interior_color = models.CharField(max_length=10,choices = INTERIOR_COLOR_CHOICES, default = "Black")
    exterior_color = models.CharField(max_length=10,choices = EXTERIOR_COLOR_CHOICES, default = "Black")
    mileage = models.IntegerField()
    slug = models.SlugField(unique=True,null = True, blank = True)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
    updated = models.DateTimeField(auto_now_add = False, auto_now = True)    
    class Meta:
        unique_together = ('model','slug')
    def get_absolute_url(self):
        return reverse("detail",kwargs={"slug":self.slug})
    def __unicode__(self):
        return self.vin_number
# It's used to be shown in single car information
class CarImage(models.Model):    
    carinfo = models.ForeignKey(CarInfo)
    carimage = models.ImageField(upload_to = 'productions/images/')
    active = models.BooleanField(default = False)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
    updated = models.DateTimeField(auto_now_add = False, auto_now = True)
    def __unicode__(self):
        return self.carinfo.vin_number
# ModelImage is for the car model which can be used to serve as the car information list images.
class ModelImage(models.Model):
    carmodel = models.ForeignKey(CarModel)
    modelimage = models.ImageField(upload_to = 'productions/images/')
    active = models.BooleanField(default = False)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
    updated = models.DateTimeField(auto_now_add = False, auto_now = True)
    def __unicode__(self):
        return self.carmodel.model
    