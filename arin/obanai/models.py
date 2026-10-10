from django.db import models
from django.contrib import admin
class User(models.Model):
    Number = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=15)
    Email = models.EmailField()
    Address = models.TextField()
    City = models.TextField()
    Pincode = models.IntegerField()
    Password = models.CharField()
    Product = models.CharField(max_length=100, default='')

class UserAdmin(admin.ModelAdmin):
    list_display = ["Number","Name","Email","Address","City","Pincode","Password","Product"]