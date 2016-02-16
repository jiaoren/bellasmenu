# Create your views here.
from django.http import  Http404, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.conf import settings
from menus.form import *
from menus.models import *
from friendship.models import Friend, Follow
from django.contrib.auth.views import password_change
from decimal import *

def main_page(request):
    if request.user.username:
        all_followings = Follow.objects.following(request.user)
        menus = Menu.objects.filter(user__in=all_followings)
    else:
        menus = Menu.objects.all()
    likedMenus = []
    profile=[]
    if request.user.is_authenticated():
        profile = request.user.get_profile()
    
    if request.user.is_authenticated():    
        for menu in menus:
            likedMenu = LikedMenu.objects.filter(menu=menu,users_liked=request.user)
            if likedMenu:
                likedMenus.append(menu)
        
    variables = RequestContext(request,{
        'menus':menus,
        'likedMenus':likedMenus,
        'username':request.user.username,
        'profile':profile,
        'requestuser':request.user.username,
        'actualuser':request.user,                            
    })
    if request.is_ajax():
        return render_to_response(
        'wrapper.html', variables,
        )
    else:
        return render_to_response(
      'main_page.html', variables,
    )
        
        
def all_page(request):
    if request.GET.has_key('category'):
        menus = Menu.objects.filter(catagory__catagoryName=request.GET.get('category'))
    elif request.GET.has_key('price_start') and request.GET.has_key('price_end'):
        menus = Menu.objects.filter(menuPrice__gte=Decimal(request.GET.get('price_start')),menuPrice__lt=Decimal(request.GET.get('price_end')))
    else:
        menus = Menu.objects.all()
    likedMenus = []
    profile=[]
    if request.user.is_authenticated():
        profile = request.user.get_profile()
    
    if request.user.is_authenticated():    
        for menu in menus:
            likedMenu = LikedMenu.objects.filter(menu=menu,users_liked=request.user)
            if likedMenu:
                likedMenus.append(menu)
        
    variables = RequestContext(request,{
        'menus':menus,
        'likedMenus':likedMenus,
        'username':request.user.username,
        'profile':profile,
        'requestuser':request.user.username,
        'actualuser':request.user,                            
    })
    if request.is_ajax():
        return render_to_response(
        'wrapper.html', variables,
        )
    else:
        return render_to_response(
      'all.html', variables,
    )
        
def popular_page(request):
    menus = Menu.objects.all().order_by('-likedmenu__likes')
    likedMenus = []
    profile=[]
    if request.user.is_authenticated():
        profile = request.user.get_profile()
    
    if request.user.is_authenticated():    
        for menu in menus:
            likedMenu = LikedMenu.objects.filter(menu=menu,users_liked=request.user)
            if likedMenu:
                likedMenus.append(menu)
        
    variables = RequestContext(request,{
        'menus':menus,
        'likedMenus':likedMenus,
        'username':request.user.username,
        'profile':profile,
        'requestuser':request.user.username,
        'actualuser':request.user,                            
    })
    if request.is_ajax():
        return render_to_response(
        'wrapper.html', variables,
        )
    else:
        return render_to_response(
      'popular.html', variables,
    )

def user_page(request, username):
    user = get_object_or_404(User, username=username)
    userself = (username == request.user.username)
    isFriend = Follow.objects.filter(follower=request.user,followee=user)
    menus = user.menu_set.order_by('-id')
    likes = LikedMenu.objects.filter(users_liked=user)
    catagories = set([menu.catagory.catagoryName for menu in menus])
    catagoryandmenu = dict()
    submenuNumber = 0
    for subcatagory in catagories:
        submenu = [menu for menu in menus if menu.catagory.catagoryName == subcatagory]
        submenuNumber += len(submenu)
        catagoryandmenu[subcatagory]=submenu
    profile = request.user.get_profile()    
    variables = RequestContext(request, {
    'menus': menus,
    'username': username,
    'catagoryandmenu':catagoryandmenu,
    'submenuNumber':submenuNumber,
    'userself':userself,
    'isFriend':isFriend,
    'user':request.user,
    'actualuser':request.user,
    'likes':len(likes),
    'profile':profile,
    'requestuser':request.user.username,
    })
    
    return render_to_response('user_page.html', variables)
   
    
def user_subpage(request, username,subpage):
    
    user = get_object_or_404(User, username=username)
    userself = (username == request.user.username)
    isFriend = Follow.objects.filter(follower=request.user,followee=user)
    if subpage == 'likes':
        likedmenus = LikedMenu.objects.filter(users_liked=user)
        menus =[likedmenu.menu for likedmenu in likedmenus]
    else:
        menus = user.menu_set.order_by('-id')
        
    likes = LikedMenu.objects.filter(users_liked=user)
    
    catagoryandmenu = set([menu.catagory.catagoryName for menu in menus])
    
    followermenus = dict()
    followingmenus = dict()
    profile = request.user.get_profile()
    all_followers = Follow.objects.followers(user)
    all_followings = Follow.objects.following(user)
    requestuser_all_followings = Follow.objects.following(request.user)
    if subpage =="followers":
        for follower in all_followers:
            followermenus[follower]=getNumberUserMenus(follower,8)
    if subpage =="following":
        for following in all_followings:
            followingmenus[following]=getNumberUserMenus(following,8)
            
    variables = RequestContext(request, {
    'menus': menus,
    'username': username,
    'catagoryandmenu':catagoryandmenu,
    'userself':userself,
    'isFriend':isFriend,
    'requestuser':request.user.username,
    'user':request.user,
    'actualuser':user,
    'likes':len(likes),
    'profile':profile,
    'subpage':subpage,
    'all_followers':all_followers,
    'followermenus':followermenus,
    'followingmenus':followingmenus,
    'requestuser_all_followings':requestuser_all_followings,
    })
    if request.is_ajax():
        return render_to_response('wrapper.html', variables,)
    else:
        return render_to_response('user_subpage.html', variables)
    
    
def getNumberUserMenus(user,amount):
    menus = user.menu_set.order_by('catagory')
    catagories = set([menu.catagory.catagoryName for menu in menus])
    numbermenus = []
    
    for subcatagory in catagories:
        submenu = [menu for menu in menus if menu.catagory.catagoryName == subcatagory]
        if len(submenu)>0:
            numbermenus.append(submenu[0])
    if len(numbermenus)> amount:
        return numbermenus[:amount]
    else:
        return numbermenus
    
def getMenusInCatagory(user,amount,catagory):
    menus = Menu.objects.filter(user=user,catagory=catagory)
    if len(menus)> amount:
        return menus[:amount]
    else:
        return menus

def getRandomMenus(amount):
    menus = Menu.objects.order_by('menuCreateTime')
    if len(menus)> amount:
        return menus[:amount]
    else:
        return menus

def catagory_page(request, username,catagoryname):
    user = get_object_or_404(User, username=username)
    catagory = get_object_or_404(Catagory,catagoryName=catagoryname)
    userself = (username == request.user.username)
    isFriend = Follow.objects.filter(follower=request.user,followee=user)
    menus = Menu.objects.filter(user=user,catagory=catagory)
    likes = LikedMenu.objects.filter(users_liked=user)
    catagories = set([menu.catagory.catagoryName for menu in menus])
    catagoryandmenu = dict()
    submenuNumber = 0
    for subcatagory in catagories:
        submenu = [menu for menu in menus if menu.catagory.catagoryName == subcatagory]
        submenuNumber += len(submenu)
        catagoryandmenu[subcatagory]=submenu
    profile = request.user.get_profile()    
    variables = RequestContext(request, {
    'menus': menus,
    'username': username,
    'catagoryandmenu':catagoryandmenu,
    'submenuNumber':submenuNumber,
    'userself':userself,
    'isFriend':isFriend,
    'user':user,
    'actualuser':request.user,
    'likes':len(likes),
    'profile':profile,
    'requestuser':request.user.username,
    'catagoryname':catagoryname,
    })
    if request.is_ajax():
        return render_to_response('wrapper.html', variables,)
    else:
        return render_to_response('catagory.html', variables)
    
    
    

def zoomscroll(request):
    if request.method =='GET':
        menuid = request.GET.get("menuid")
    if menuid:
        menu = Menu.objects.get(id=menuid)
        user = menu.user
        catagory = menu.catagory
        menuinsamecatagory = getMenusInCatagory(user,12,catagory)
        originalpostedmenus = getNumberUserMenus(user,5)
        newlyuploaded = getRandomMenus(5)
    variables = RequestContext(request,{
                               'menu':menu,
                               'user':user,
                               'catagory':catagory,
                               'actualuser':user,
                               'menuinsamecatagory':menuinsamecatagory,
                               'originalpostedmenus':originalpostedmenus,
                               'newlyuploaded':newlyuploaded,})
    return render_to_response('zoomscroll.html', variables)
    
def takeit(request):
    if request.method =='GET':
        menuid = request.GET.get("menuid")
    if menuid:
        menu = Menu.objects.get(id=menuid)
        user = menu.user
        catagories = Catagory.objects.all()
    variables = RequestContext(request,{
                               'menu':menu,
                               'user':user,
                               'actualuser':user,
                               'catagories':catagories,})
    return render_to_response('takeit.html', variables)

@login_required
def posttakeit(request):
    
    catagory = request.GET.get("catagory")
    takeit_menu_id = request.GET.get("takeit_menu_id")
    details = request.GET.get("details")
    originalmenu = Menu.objects.get(id=takeit_menu_id)
    if(catagory != originalmenu.catagory.catagoryName):
        originalmenu.catagory = Catagory.objects.get(catagoryName=catagory)
    originalmenu.menuDescription = details
    originalmenu.user = request.user
    newcatagory = originalmenu.catagory.catagoryName
    try:
        originalmenu.id = None
        variables = RequestContext(request,{
                               'menu':originalmenu,
                               'user':request.user,
                               'catagory1':newcatagory,})
        originalmenu.save()
        return render_to_response('posttakeit.html', variables)
    except:
        return HttpResponse('false')

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')



def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username =form.cleaned_data['username'],
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password1']
            )
            return HttpResponseRedirect('/login')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
            'form': form,
            'username':request.user.username,
        })
    return render_to_response(
            'registration/register.html',variables)
        

@login_required
def menuSubmit_page(request):
    if request.method == 'POST':
        form = SubmitMenuForm(request.POST,request.FILES)
        if form.is_valid():
            catagory,createdCatagory = Catagory.objects.get_or_create(catagoryName=form.cleaned_data['menuCatagory'])
            restaurant,createdRes = Restaurant.objects.get_or_create(ResName=form.cleaned_data['restaurant'],ResType=catagory)
            
            menu,createdMenu = Menu.objects.get_or_create(menuName=form.cleaned_data['menuName'],
                                                     menuPrice=form.cleaned_data['menuPrice'],
                                                     menuStar=form.cleaned_data['menuStar'],
                                                     menuPics=form.cleaned_data['menuPic'],
                                                     menuDescription=form.cleaned_data['menuDescription'],
                                                     restaurant = restaurant,
                                                     catagory = catagory,
                                                     user=request.user,)
            menu.menuPics.name = menu.menuPics.name.split('/')[-1]
            menu.save()
            return HttpResponseRedirect('/user/%s/' % request.user.username)
    
    else:
        form = SubmitMenuForm()
    variables = RequestContext(request, {
            'form': form
    })
    return render_to_response('menuSubmit_page.html', variables)

def search_page(request):
    
    menus = []
    if request.GET.has_key('query'):
        query = request.GET['query'].strip()
        if query:
            menus = Menu.objects.filter(menuName__icontains=query)
       
    likedMenus = []
    profile=[]
    if request.user.is_authenticated():
        profile = request.user.get_profile()
    
    if request.user.is_authenticated():    
        for menu in menus:
            likedMenu = LikedMenu.objects.filter(menu=menu,users_liked=request.user)
            if likedMenu:
                likedMenus.append(menu)
                
    variables = RequestContext(request,{
        'menus':menus,
        'likedMenus':likedMenus,
        'username':request.user.username,
        'profile':profile,
        'requestuser':request.user.username,
        'actualuser':request.user,                            
    })
    if request.is_ajax():
        return render_to_response('wrapper.html', variables,)
    else:
        return render_to_response('search.html', variables,)


def ajax_search_autocomplete(request):
    if request.GET.has_key('q'):
        menus = Menu.objects.filter(menuName__istartswith=request.GET['q'])[:10]
        return HttpResponse('\n'.join(menu.menuName for menu in menus))
    return HttpResponse()

@login_required
def ajax_like(request):
    if request.GET.has_key('q'):
        query = request.GET['q'].strip()
        if query:
            menu = Menu.objects.get(pk=query)
            user = request.user
            likedMenu,created = LikedMenu.objects.get_or_create(menu=menu)
            if created:
                likedMenu.likes = 1
                likedMenu.users_liked.add(request.user)
            else:
                user_liked = likedMenu.users_liked.filter(username=request.user.username)
                if not user_liked:
                    likedMenu.likes = likedMenu.likes + 1
                    likedMenu.users_liked.add(request.user)
            likedMenu.save()
            return HttpResponse("true")

@login_required
def ajax_unlike(request):
    if request.GET.has_key('q'):
        query = request.GET['q'].strip()
        if query:
            menu = Menu.objects.get(pk=query)
            user = request.user
            likedMenu= LikedMenu.objects.get(menu=menu,users_liked=user)
            if likedMenu:
                likes = likedMenu.likes - 1
                likedMenu.likes = likes
                likedMenu.save()
                likedMenu.users_liked.remove(request.user)
                if likes == 0:
                    likedMenu.delete()
            
            return HttpResponse("true")


def ajax_edit_about(request):
    if request.method == 'GET':
        about = request.GET.get('description')
        if about:
            profile = request.user.get_profile()
            try:
                profile.about = about
                profile.save()
                return HttpResponse("true")
            except:
                return HttpResponse("false")


@login_required
def follow(request,username):
    if username:
        followee = get_object_or_404(User, username=username)
        following_created = Follow.objects.add_follower(request.user, followee)
        return HttpResponse("true")
    else:
        raise Http404 
    
def unfollow(request,username):
    if username:
        followee = get_object_or_404(User, username=username)
        isFriend = Follow.objects.filter(follower=request.user,followee=followee)
        if isFriend:
            was_following = Follow.objects.remove_follower(request.user, followee)
            return HttpResponse("true")
    else:
        raise Http404 
        
@login_required
def edit_profile(request,username):
    
    if request.method == 'POST':
        
        if request.POST.has_key("loginwithfb"):
            loginwithfb = request.POST["loginwithfb"]
        else:
            loginwithfb = "off"
            
        if request.POST.has_key("posttofbtimeline"):
            posttofbtimeline = request.POST["posttofbtimeline"]
        else:
            posttofbtimeline = "off"
            
        if request.POST.has_key("loginwithtwitter"):
            loginwithtwitter = request.POST["loginwithtwitter"]
        else:
            loginwithtwitter = "off"
            
        profile1request = {"firstname":request.POST["firstname"],
            "lastname": request.POST["lastname"],
            "gender": request.POST["gender"],
            "avatar":"C:\\temp\\covhub.png",
            "location": request.POST["location"],
            "about": request.POST["about"],
            "loginwithfb":loginwithfb,
            "posttofbtimeline":posttofbtimeline,
            "loginwithtwitter":loginwithtwitter,
            "language":request.POST["language"]}
        
        emailform = {
                     'email':request.POST['email'],
                     }
        usernameform = {
                     'username':request.POST['username'],
                     }
        profileForm1 = ProfileForm1(profile1request,request.FILES)
        userEmailForm = UserEmailForm(emailform,instance=request.user)
        usernameForm = UsernameForm(usernameform,instance=request.user)
        if profileForm1.is_valid() and userEmailForm.is_valid() and usernameForm.is_valid():
            userEmailForm.save()
            usernameForm.save()
            profile = request.user.get_profile()
            profile.firstname = profileForm1.cleaned_data['firstname']
            profile.lastname = profileForm1.cleaned_data['lastname']
            profile.gender = profileForm1.cleaned_data['gender']
            profile.location = profileForm1.cleaned_data['location']
            profile.about = profileForm1.cleaned_data['about']
            if profileForm1.cleaned_data['avatar']:
                profile.avatar = profileForm1.cleaned_data['avatar']
            else:
                pass
            profile.loginwithfb = profile1request['loginwithfb'] if profile1request['loginwithfb']!='off' else False
            profile.posttofbtimeline = profile1request['posttofbtimeline'] if profile1request['posttofbtimeline']!='off' else False
            profile.loginwithtwitter = profile1request['loginwithtwitter'] if profile1request['loginwithtwitter']!='off' else False
            profile.language = profileForm1.cleaned_data['language']
            profile.save()
            profile.avatar = "avatar/"+profile.avatar.__str__().split('/')[-1]
            profile.save()
            return HttpResponseRedirect("/user/%s" % request.user.username)
        
        
    else:
        
        profileForm1 = ProfileForm1()
        userEmailForm = UserEmailForm()
        usernameForm = UsernameForm()
        
        userEmailForm.fields['email'].initial=request.user.email
        usernameForm.fields['username'].initial=request.user.username
        profile = request.user.get_profile()
        
        profileForm1.fields['lastname'].initial = profile.lastname
        profileForm1.fields['firstname'].initial = profile.firstname
        profileForm1.fields['gender'].initial = profile.gender
        profileForm1.fields['location'].initial = profile.location
        profileForm1.fields['about'].initial = profile.about
        profileForm1.fields['loginwithfb'].initial = profile.loginwithfb
        profileForm1.fields['posttofbtimeline'].initial = profile.posttofbtimeline
        profileForm1.fields['loginwithtwitter'].initial = profile.loginwithtwitter
        
        
    profile = request.user.get_profile()
    variables = RequestContext(request, {
        'profileForm1': profileForm1,
        'userEmailForm':userEmailForm,
        'usernameForm':usernameForm,
        'profile':profile,
        'username':request.user.username,
        'requestuser':request.user.username,
    })
    return render_to_response('editprofile.html',variables)

@login_required    
def changepassword(request,template_name='changepassword.html'):
    
    return password_change(request, template_name,post_change_redirect='/user/'+request.user.username)

@login_required
def emailsettings(request):
    
    if request.method == 'POST':
        myrequestpost = {
                         'emailOnComments': request.POST["emailOnComments"] if request.POST.has_key("emailOnComments") else 'off',
                         'emailOnLikes': request.POST["emailOnLikes"] if request.POST.has_key("emailOnLikes") else 'off',
                         'emailOnTakeIt' : request.POST["emailOnTakeIt"] if request.POST.has_key("emailOnTakeIt") else 'off',
                         'emailOnRecommend': request.POST["emailOnRecommend"] if request.POST.has_key("emailOnRecommend") else 'off',
                         'emailOnFollows': request.POST["emailOnFollows"] if request.POST.has_key("emailOnFollows") else 'off',
                         'emailFrequency':request.POST["emailFrequency"] if request.POST.has_key("emailFrequency") else '0',
                         'emailDigest':request.POST["emailDigest"] if request.POST.has_key("emailDigest") else 'off',
                         'emailNewsUpdates':request.POST["emailNewsUpdates"] if request.POST.has_key("emailNewsUpdates") else 'off',      
                         }
        profileForm2 = ProfileForm2(myrequestpost)
        
        if profileForm2.is_valid():
            profile = request.user.get_profile()
            profile.emailOnComments = myrequestpost['emailOnComments'] if myrequestpost['emailOnComments']!='off'  else False
            profile.emailOnLikes = myrequestpost['emailOnLikes'] if myrequestpost['emailOnLikes']!='off' else False
            profile.emailOnTakeIt = myrequestpost['emailOnTakeIt'] if myrequestpost['emailOnTakeIt']!='off' else False
            profile.emailOnRecommend = myrequestpost['emailOnRecommend'] if myrequestpost['emailOnRecommend']!='off' else False
            profile.emailOnFollows = myrequestpost['emailOnFollows'] if myrequestpost['emailOnFollows']!='off' else False
            profile.emailFrequency = myrequestpost['emailFrequency'] if myrequestpost['emailFrequency']!='0' else '0'
            profile.emailDigest = myrequestpost['emailDigest'] if myrequestpost['emailDigest']!='off' else False
            profile.emailNewsUpdates = myrequestpost['emailNewsUpdates'] if myrequestpost['emailNewsUpdates']!='off' else False
            profile.save()
            return HttpResponseRedirect('/user/%s' % request.user.username)
            
        else:
            return HttpResponse(profileForm2.cleaned_data['emailOnComments'])
            
    else:
        profileForm2 = ProfileForm2()
        profile = request.user.get_profile()
        profileForm2.fields['emailOnComments'].initial = profile.emailOnComments
        profileForm2.fields['emailOnLikes'].initial = profile.emailOnLikes
        profileForm2.fields['emailOnTakeIt'].initial = profile.emailOnTakeIt
        profileForm2.fields['emailOnRecommend'].initial = profile.emailOnRecommend
        profileForm2.fields['emailOnFollows'].initial = profile.emailOnFollows
        profileForm2.fields['emailFrequency'].initial = '1'
        profileForm2.fields['emailDigest'].initial = profile.emailDigest
        profileForm2.fields['emailNewsUpdates'].initial = profile.emailNewsUpdates
    
        
    variables = RequestContext(request, {
        'profileForm2':profileForm2,
        'email':request.user.email,
        'username':request.user.username,
        
    })
    return render_to_response('emailsettings.html',variables)

    
@login_required
def deactivate(request):
    
    user = User.objects.get(username=request.user.username)
    user.is_active=True
    user.save()
    return HttpResponseRedirect('/')
    
    
def entry_index(request,
    template="wrapper.html",
    page_template="wrapper.html"):
    context = {
        'objects': Menu.objects.all(),
        'page_template': page_template,
    }
    if request.is_ajax():
        template = page_template
    return render_to_response(template, context,
        context_instance=RequestContext(request))
    
def about_page(request):
    variables = RequestContext(request, {
            'requestuser':request.user.username,
            'subpage':None,
        })
    return render_to_response(
            'about.html',variables)
    
def about_subpage(request,subpage):
    variables = RequestContext(request, {
            'requestuser':request.user.username,
            'subpage':subpage,
        })
    return render_to_response(
            'about.html',variables)

def reservation(request):
    if request.user.username:
        all_followings = Follow.objects.following(request.user)
        menus = Menu.objects.filter(user__in=all_followings)
    else:
        menus = Menu.objects.all()
    likedMenus = []
    profile=[]
    if request.user.is_authenticated():
        profile = request.user.get_profile()
    
    if request.user.is_authenticated():    
        for menu in menus:
            likedMenu = LikedMenu.objects.filter(menu=menu,users_liked=request.user)
            if likedMenu:
                likedMenus.append(menu)
        
    variables = RequestContext(request,{
        'menus':menus,
        'likedMenus':likedMenus,
        'username':request.user.username,
        'profile':profile,
        'requestuser':request.user.username,
        'actualuser':request.user,                            
    })
    if request.is_ajax():
        return render_to_response(
        'wrapper.html', variables,
        )
    else:
        return render_to_response(
      'reservation.html', variables,
    )
