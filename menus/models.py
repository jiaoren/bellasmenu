from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Catagory(models.Model):
    catagoryName = models.CharField(max_length=255)
    
class Restaurant(models.Model):
    ResName = models.CharField(max_length=255)
    ResLocation = models.CharField(max_length=255)
    ResPhone = models.CharField(max_length=20)
    ResType = models.ForeignKey(Catagory)
    
class Menu(models.Model):
    menuName = models.CharField(max_length=255)
    menuPrice = models.DecimalField(max_digits=5,decimal_places=2)
    menuCreateTime = models.DateTimeField(auto_now=True)
    menuStar = models.IntegerField()
    menuPics = models.ImageField(upload_to=settings.STATIC_ROOT)
    menuDescription = models.CharField(max_length=255)
    catagory = models.ForeignKey(Catagory)
    restaurant = models.ForeignKey(Restaurant)
    user = models.ForeignKey(User)
    
class LikedMenu(models.Model):
    menu = models.ForeignKey(Menu,unique=True)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=1)
    users_liked = models.ManyToManyField(User)
    def __str__(self):
        return '%s, %s' % self.menu, self.likes
    
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    gender = models.CharField(max_length=50,default="2")
    about = models.CharField(max_length=124,blank=True)
    location = models.CharField(max_length=100,blank=True)
    avatar = models.ImageField(upload_to=settings.STATIC_ROOT+"/avatar")
    loginwithfb = models.BooleanField(default=True)
    posttofbtimeline = models.BooleanField(default=True)
    loginwithtwitter = models.BooleanField(default=False)
    accoutStatus = models.BooleanField(default=False)
    emailOnComments = models.BooleanField(default=True)
    emailOnLikes = models.BooleanField(default=True)
    emailOnTakeIt = models.BooleanField(default=True)
    emailOnRecommend = models.BooleanField(default=True)
    emailOnFollows = models.BooleanField(default=True)
    emailFrequency = models.CharField(max_length=10,default="0")
    emailDigest = models.BooleanField(default=True)
    emailNewsUpdates = models.BooleanField(default=True)
    language = models.CharField(max_length=20,default="English")
    
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
post_save.connect(create_user_profile, sender=User)

from social_auth.signals import pre_update
from social_auth.backends.facebook import FacebookBackend
from social_auth.signals import socialauth_registered
import urllib
def facebook_extra_values(sender, user, response, details, **kwargs):
    profile,create = UserProfile.objects.get_or_create(user=user)
    profile.gender = response['gender']
    profile.firstname = response['first_name']
    profile.lastname = response['last_name']
    profile.loginwithfb = True
    profile.loginwithtwitter = False
    url = "http://graph.facebook.com/%s/picture?type=large" % response['id']
    avatar = urllib.urlopen(url).read()
    fout = open(settings.STATIC_ROOT+"/avatar/"+response['first_name']+'_'+response['last_name']+'_'+response['id'], "wb")
    fout.write(avatar)
    fout.close()
    profile.avatar = "avatar/"+response['first_name']+'_'+response['last_name']+'_'+response['id']
    profile.save()
    return True

pre_update.connect(facebook_extra_values, sender=FacebookBackend)

from social_auth.backends.twitter import TwitterBackend
def twitter_user_update(sender, user, response, details, **kwargs):
    profile, create = UserProfile.objects.get_or_create(user=user)
    try:
        first_name,last_name = response['name'].split(' ',1)
    except:
        first_name = response['name']
        last_name = ''
    profile.firstname = first_name
    profile.lastname = last_name
    profile.loginwithfb = False
    profile.loginwithtwitter = True
    url = response['profile_image_url']
    avatar = urllib.urlopen(url).read()
    fout = open(settings.STATIC_ROOT+"/avatar/"+first_name+"_"+last_name+"_"+response['id_str']+".jpg", "wb")
    fout.write(avatar)
    fout.close()
    profile.avatar = "avatar/"+first_name+"_"+last_name+"_"+response['id_str']+".jpg"
    profile.save()
    return True

pre_update.connect(twitter_user_update, sender=TwitterBackend)
