
from django.db import models
from django.contrib import admin
class User(models.Model):
    Number = models.IntegerField(max_length=15, primary_key=True)
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Address = models.TextField()
    City = models.CharField(max_length=50)
    Pincode = models.IntegerField()
    Password = models.CharField(max_length=100)
class UserAdmin(admin.ModelAdmin):
    list_display = ["Number","Name","Email","Address","City","Pincode","Password"]
