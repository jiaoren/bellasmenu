from django.conf.urls import patterns, include, url
from menus.views import *
import os.path
from django.views.generic.simple import direct_to_template
from django.conf import settings
from django.contrib.auth.views import password_change

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

site_media = os.path.join(
  os.path.dirname(__file__), 'site_media'
)



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'socialmenu.views.home', name='home'),
    # url(r'^socialmenu/', include('socialmenu.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^$',main_page),
    (r'^popular/$',popular_page),
    (r'^all/$',all_page),
    (r'^user/(\w+)/$',user_page),
    (r'^user/(\w+)/(\w+)/$',user_subpage),
    (r'^menu/takeit/$',takeit),
    (r'^posttakeit/$',posttakeit),
    (r'^(\w+)/catagory/(\w+)/$',catagory_page),
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', logout_page),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
    { 'document_root': site_media }),
    (r'^images/(?P<path>.*)$', 'django.views.static.serve',
    { 'document_root': settings.STATIC_ROOT }),
    (r'^register/$', register_page),
    (r'^submit_menu/$',menuSubmit_page),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^search/$', search_page),
    (r'^ajax/search/autocomplete/$', ajax_search_autocomplete),
    (r'^ajax_like',ajax_like),
    (r'^ajax_unlike',ajax_unlike),
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^follow/(\w+)/$', follow),
    (r'^unfollow/(\w+)/$', unfollow),
    (r'^edit_profile/(\w+)/$',edit_profile),
    (r'^password/change/$',changepassword),
    (r'^prefs/$',emailsettings),
    (r'^delete/$',deactivate),
    (r'^zoomscroll/$',zoomscroll),
    (r'^ajax_edit_about/$',ajax_edit_about),
    (r'^about/$',about_page),
    (r'^about/(\w+)/$',about_subpage),
    (r'',include('social_auth.urls')),  
    (r'^reservation',reservation),
)
