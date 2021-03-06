from os import name
from allauth.account.views import LogoutView, SignupView
from django.contrib import admin
from django import urls
from django.urls import path
from .views import listview,LoginView,secret,detailview ,listwordview,CommentCreate,Delete,commentDelete, CreateClass, signup, LogoutVieww #find ,loginvuew, SignupView

app_name='printapp'
urlpatterns = [
    path('list/',listview,name='list'),
    #path('signup/',signupview,name='signup'),
    #path('',loginview,name='login'),
    #path('', LoginView.as_view(), name='login'),
    path('', secret, name='secret'),
    path('hwuy789ty79ysgheuy9gyo8t8gos8eg8osehew5uw4uhuwqh4/', SignupView.as_view(), name='signup'),
    path('logout/', LogoutVieww.as_view(), name='logout'),
    path('create/', CreateClass.as_view(), name='create'),
    path('delete/<int:pk>', Delete, name='delete'),
    path('find/', listwordview, name='find'),
    path('detail/<int:pk>', detailview, name='detail'),
    path('commentdelete/<int:pk>',commentDelete,name='deletecomment'),
    path('comment/<int:pk>', CommentCreate.as_view(), name='comment_create'),  
]