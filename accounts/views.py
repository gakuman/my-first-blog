from printapp.models import PrintModel
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth import get_user_model
from django.db import IntegrityError
from django.contrib.auth import authenticate,login,logout
from django.views.generic import CreateView,ListView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import User_user
from django.views import View
from accounts.forms import ProfileForm
from printapp.models import PrintModel

@login_required
def user_profile(request, username):
    object_list = PrintModel.objects.all()
    User = get_user_model().objects.get(username=username)
    """ context = {
        'User':get_user_model().objects.get(username=username),
        'object_list':PrintModel.objects.all(),
    } """
    return render(request, 'accounts/user_profile.html', {'object_list':object_list,'User':User})



class Profile_editview(View):
    def get(self, request, *args, **kwargs):
        user_data = User_user.objects.get(id=request.user.id)
        form = ProfileForm(
            request.POST or None,
            initial={
                'name':user_data.username,
                'icon':user_data.icon,
                'introduction':user_data.introduction,
            }
        )

        return render(request, 'accounts/profile_edit.html',{'form':form})

    def post(self, request, *args, **kwargs):
        form = ProfileForm(request.POST or None)
        if form.is_valid():
            user_data = User_user.objects.get(id=request.user.id)
            user_data.username = form.cleaned_data['name']
            user_data.icon = form.cleaned_data['icon']
            user_data.introduction = form.cleaned_data['introduction']
            user_data.save()
            return redirect('printapp:list')
        
        return render(request, 'printapp/list.html', {
            'form':form
        })



