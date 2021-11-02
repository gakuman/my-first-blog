from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate,login,logout
from django.views.generic import CreateView,ListView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from accounts.models import User_user,UserManager
from allauth.account import views
from accounts.forms import SignupUserForm,secretform,Findform
from printapp.models import PrintModel
from django.contrib.auth import get_user_model


""" @login_required
def listview(request):
    object_list = PrintModel.objects.all().order_by('id').reverse()
    return render(request,'printapp/list.html',{'object_list':object_list})
 """
class CreateClass(CreateView):
    template_name = 'printapp/create.html'
    model = PrintModel
    fields = ('title','content','images','author','category')
    success_url = reverse_lazy('printapp:list')


@login_required
def listview(request):
    if request.method == 'POST':
        form = Findform(request.POST)
        find = request.POST['find']
        if find == '全て':
            data = PrintModel.objects.all().order_by('id').reverse()
        else:
            data = PrintModel.objects.filter(category=find).order_by('id').reverse()
    else:
        form = Findform()
        data = PrintModel.objects.all().order_by('id').reverse()
    context = {
        'form':form,
        'data':data
    }
    return render(request, 'printapp/list.html',context)



""" def signupview(request):
    message = 'アカウント作成'
    if request.method == 'POST':
        username_data = request.POST['name']
        mail_data = request.POST['mail']
        password_data = request.POST['password']
        secret = request.POST['secret']
        try:
            a = User_user(username=username_data, password=password_data,email=mail_data)
            a.save()
        except IntegrityError:
            return render(request, 'printapp/signup.html',{'error':'このアカウントは既に登録されています。'})

        if secret == 'kitano':
            return redirect('printapp:list')
        else:
            u = User_user.objects.get(username = username_data)
            u.delete()
            return render(request,'printapp/signup.html',{'message':'秘密のパスワードが違います'})

    else:
        return render(request, 'printapp/signup.html',{'message':message})
    return render(request, 'printapp/signup.html',{'message':message})
 
 """





""" def loginview(request):
    if request.method == 'POST':
        username_data = request.POST['name']
        password_data = request.POST['password']
        user = authenticate(request, username=username_data, password=password_data)

        if user is not None:
            login(request, user)
            return redirect('printapp:list')
        else:
            return render(request, 'printapp/login.html', {'message':'アカウントが存在しません。'})
    
    return render(request, 'printapp/login.html',{'message':'ログイン画面'}) """


#class SignupView(views.SignupView):
    #template_name = 'printapp/signup2.html'
    #form_class = SignupUserForm


class Delete(DeleteView):
    template_name = 'delete.html'
    model = PrintModel
    success_url = reverse_lazy('printapp:list')





class LoginView(views.LoginView):
    template_name = 'printapp/login2.html'

class LogoutVieww(views.LogoutView):
    template_name = 'printapp/logout.html'

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            self.logout()
        return redirect('/hwuy789ty79ysgheuy9gyo8t8gos8eg8osehew5uw4uhuwqh4/')


def secret(request):
    form = secretform
    if request.method == 'POST':
        word = request.POST['secret']
        if word == 'kitano':
            return redirect('/hwuy789ty79ysgheuy9gyo8t8gos8eg8osehew5uw4uhuwqh4/')
        
    else:
        return render(request,'printapp/secret.html', {'form':form})
    return render(request,'printapp/secret.html', {'form':form})


def signup(request):
    if request.method == 'POST':
        form = SignupUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignupUserForm()
    return render(request, 'printapp/signup2.html', {'form': form})


