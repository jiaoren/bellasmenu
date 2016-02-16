'''
Created on Jun 5, 2012

@author: hxia
'''
from django import forms
from django.db import models
from django.forms import extras
import re
from django.contrib.auth.models import User
from models import *
from django.core.exceptions import ObjectDoesNotExist


class RegistrationForm(forms.Form):
    username = forms.CharField(label='Name',max_length=30)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(
       label='Password',
       widget=forms.PasswordInput()
    )

    password2 = forms.CharField(
       label='Reenter Password',
       widget=forms.PasswordInput()
    )
    
    
    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                return password2
        raise forms.ValidationError('Passwords do not match.')
    
    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            User.objects.get(email=email)
        except ObjectDoesNotExist:
            return email
        raise forms.ValidationError('Email is already taken.')
    
    
class SubmitMenuForm(forms.Form,):
    menuPic = forms.ImageField(label='Image');
    menuName = forms.CharField(label='Name',max_length=30,widget=forms.TextInput(attrs={'size': 32}))
    menuCatagory = forms.ChoiceField(label='Catagory',choices=(('Chinese','Chinese'),('American','American'),('Mexcico','Mexcico'),('Japanese','Japanese'),('Korean','Korean'),('Other','Other'),),initial='Chinese')
    restaurant = forms.CharField(label='Restaurant',max_length=30,widget=forms.TextInput(attrs={'size': 32}))
    menuPrice = forms.DecimalField(label='Price',max_digits=5,decimal_places=2,widget=forms.TextInput(attrs={'size': 5}))
    menuStar = forms.ChoiceField(label='Stars',choices=((0,'0 star'),(1,'1 star'),(2,'2 star'),(3,'3 star'),(4,'4 star'),(5,'5 star'),),initial='0')
    menuDescription = forms.CharField(label='Description',max_length=256,widget=forms.TextInput(attrs={'size': 32}))

class SearchForm(forms.Form):
    query = forms.CharField(
        label='Enter a keyword to search for',
        widget=forms.TextInput(attrs={'size': 32,'class':'ui-autocomplete-input default_value placeholder'})
    )
  
class ProfileForm(forms.Form):

    firstname = forms.CharField(max_length=25)
    lastname = forms.CharField(max_length=25)
    gender = forms.ChoiceField(choices=((0,'Male'),(1,'Female'),(2,'Unspecified')),initial='2',widget=forms.RadioSelect())
    location = forms.CharField(max_length=100,required=False)
    about = forms.CharField(required=False,widget=forms.Textarea(attrs={'cols':54,'rows':3}))
#    avatar = forms.ImageField(widget=forms.ClearableFileInput(attrs={"id":"id_img","name":"img","size":6}))
    loginwithfb = forms.BooleanField(widget=forms.CheckboxInput(attrs={'style':'display:none','id':'facebook_connect'}))
    posttofbtimeline = forms.BooleanField(widget=forms.CheckboxInput(attrs={'style':'display:none','id':'facebook_timeline'}))
    loginwithtwitter = forms.BooleanField(widget=forms.CheckboxInput(attrs={'style':'display:none','id':'twitter_connect'}))
    accoutStatus = forms.BooleanField()
    emailOnComments = forms.BooleanField()
    emailOnLikes = forms.BooleanField()
    emailOnTakeIt = forms.BooleanField()
    emailOnRecommend = forms.BooleanField()
    emailOnFollows = forms.BooleanField()
    emailFrequency = forms.ChoiceField(choices=((0,'Immediatly'),(1,'Daily')),initial='0',widget=forms.RadioSelect())
    emailDigset = forms.BooleanField()
    emailNewsUpdates = forms.BooleanField()
    language = forms.ChoiceField(choices=((0,'English'),(1,'Chinese')),initial='0')
    
class UserEmailForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('email',)
    def clean_email(self):
        """
        Verify that the email exists
        """
        email = self.cleaned_data.get("email")

        if not email: 
            return  email

        if User.objects.filter(email__iexact=email).exclude(pk=self.instance.pk):
            raise forms.ValidationError("That e-mail is already used.")
        else:
            return email
    

class UsernameForm(forms.ModelForm):
    username = forms.CharField(max_length=30,required=True)
    
    class Meta:
        model = User
        fields = ('username',)
    def clean_username(self):
        """
        Verify that the email exists
        """
        username = self.cleaned_data.get("username")

        if not username: 
            return  username

        
        if User.objects.filter(username__iexact=username).exclude(pk=self.instance.pk):
            raise forms.ValidationError("That username is already used.")
        else:
            return username
        
class ProfileForm1(forms.ModelForm):
    
    firstname = forms.CharField(max_length=25)
    lastname = forms.CharField(max_length=25)
    language = forms.ChoiceField(choices=((0,'English'),(1,'Chinese')),initial='0')
    gender = forms.ChoiceField(choices=((0,'Male'),(1,'Female'),(2,'Unspecified')),initial='2',widget=forms.RadioSelect())
    location = forms.CharField(max_length=100,required=False)
    about = forms.CharField(required=False,widget=forms.Textarea(attrs={'cols':54,'rows':3}))
    avatar = forms.ImageField(widget=forms.FileInput(attrs={"id":"id_img","size":6}),required=False)
    loginwithfb = forms.BooleanField(widget=forms.CheckboxInput(attrs={'style':'display:none','id':'facebook_connect'}))
    posttofbtimeline = forms.BooleanField(widget=forms.CheckboxInput(attrs={'style':'display:none','id':'facebook_timeline'}))
    loginwithtwitter = forms.BooleanField(widget=forms.CheckboxInput(attrs={'style':'display:none','id':'twitter_connect'}))
    class Meta:
        model = UserProfile
        fields = ('firstname','lastname','gender','location','about','loginwithfb','posttofbtimeline','loginwithtwitter','language','avatar',)

class ProfileForm2(forms.ModelForm):
    
#    accoutStatus = forms.BooleanField()
    emailOnComments = forms.BooleanField(widget=forms.CheckboxInput(attrs={'style':'display:none','id':'id_email_comments'}))
    emailOnLikes = forms.BooleanField(widget=forms.CheckboxInput(attrs={'style':'display:none','id':'id_email_likes'}))
    emailOnTakeIt = forms.BooleanField(widget=forms.CheckboxInput(attrs={'style':'display:none','id':'id_email_takeit'}))
    emailOnRecommend = forms.BooleanField(widget=forms.CheckboxInput(attrs={'style':'display:none','id':'id_email_recommend'}))
    emailOnFollows = forms.BooleanField(widget=forms.CheckboxInput(attrs={'style':'display:none','id':'id_email_follows'}))
    emailFrequency = forms.ChoiceField(choices=((0,'Immediatly'),(1,'Daily')),initial='0',widget=forms.RadioSelect(attrs={'id':'theFrequency'}))
    emailDigest = forms.BooleanField(widget=forms.CheckboxInput(attrs={'style':'display:none','id':'id_email_digest'}))
    emailNewsUpdates = forms.BooleanField(widget=forms.CheckboxInput(attrs={'style':'display:none','id':'id_email_news'}))
    class Meta:
        model = UserProfile
        fields = ('accoutStatus','emailOnComments','emailOnLikes','emailOnTakeIt','emailOnRecommend','emailOnFollows','emailFrequency','emailDigest','emailNewsUpdates',)

class DeactivateForm(forms.ModelForm):
    is_active = forms.BooleanField(widget=forms.CheckboxInput(attrs={'id':'enable_button'}))
    
    class Meta:
        model = User
        fields = ('is_active',)
        
    