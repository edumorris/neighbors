from django.db import models

from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import *
from django.contrib.auth.models import User

# Create your models here.
class Neighborhood(models.Model):
    neighborhood_name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    occupants = models.IntegerField()
    Admin = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.neighborhoob_name
    
    def save_neighborhood(self):
        self.save()
    
    def delete_neighborhood(self):
        self.delete()
    
    def update_profile(self):
        pass

class Profile(models.Model):
    user = models.OneToOneField(User, blank=True, default=0000, on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField()
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, blank=True, null=True)
    phone_number = models.CharField(max_length =15, blank = True)
    status = models.CharField(max_length = 15)

    def __str__(self):
        return self.first_name
    
    def save_profile(self):
        self.save()
    
    def delete_profile(self):
        self.delete()
    
    def update_profile(self):
        pass
    
    @receiver(post_save, sender=User)
    def create_or_update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

class Business(models.Model):
    business_name = models.CharField(max_length=150)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)

    def __str__(self):
        return self.business_name
    
    def save_business(self):
        self.save()
    
    def delete_business(self):
        self.delete()
    
    def update_business(self):
        pass

class Contact(models.Model):
    contant_owner = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    contact_category = models.CharField(max_length=50)

    def __str__(self):
        return self.contant_owner
    
    def save_contact(self):
        self.save()
    
    def delete_contact(self):
        self.delete()
    
    def update_contact(self):
        pass