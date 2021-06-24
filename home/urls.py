#from django.contrib import admin
from django.urls import path
#from django.conf.urls import url
#from home import views
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home, name='home'),
    path("home", views.home, name='home'),
    path("contact", views.contact, name='contact'),
    path("tutorials", views.tutorials, name='tutorials'),
    path("services", views.services, name='services'),
    path("upload_files", views.upload_files, name='upload_files'),
    path("about", views.about, name='about'),
    path("registration", views.registration, name='registration'),
    path("login", views.login, name='login'),
    path("logout", views.logout, name='logout'),
    path("search", views.search_services, name='search'),
    path("addscriptfile", views.addscript, name='addscriptfile'),
    path("deleteScript/<pk>", views.deleteScript, name='deleteScript'),
    path("manual_page", views.manual_page, name='manual_page'),
    path("tutorial_view/<pk>", views.tutorial_view,name="tutorial_view"),
    path("update_script/<pk>",views.update_script,name='update_script'),
    path("edit_script/<pk>",views.edit_script,name='edit_script'),
    


#Password change urls: 

    path("password_change/done/", auth_views.PasswordChangeDoneView.as_view(template_name='password/password_change_done.htm'), name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password/password_change.htm'), name='password_change'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password/password_reset_form.htm'), name='password_reset'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_done.htm'),name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password/password_reset_confirm.htm'), name='password_reset_confirm'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.htm'), name='password_reset_complete')

#Password change urls: Completed
]
