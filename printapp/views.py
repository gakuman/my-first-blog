from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate,login,logout
from django.views.generic import CreateView,ListView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from accounts.models import User_user,UserManager
from allauth.account import views
from accounts.forms import SignupUserForm,secretform,Findform,CommentCreateForm,WordForm
from printapp.models import PrintModel
from django.contrib.auth import get_user_model
from printapp.models import Comment
from django.shortcuts import get_object_or_404
from django.db.models import Q


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
    if request.user.is_superuser:
        admin = 'OK'
    else:
        admin = 'NO'
    if request.method == 'POST':
        form = Findform(request.POST)
        find = request.POST['find']
        if find == '全て':
            data = PrintModel.objects.all().order_by('id').reverse()
            c_num = PrintModel.objects.all().count()

        else:
            data = PrintModel.objects.filter(category=find).order_by('id').reverse()
            c_num = PrintModel.objects.filter(category=find).count()
    else:
        form = Findform()
        data = PrintModel.objects.all().order_by('id').reverse()
        c_num = PrintModel.objects.all().count()

    context = {
        'form':form,
        'data':data,
        'admin':admin,
        'count':c_num
    }
    return render(request, 'printapp/list.html',context)



@login_required
def listwordview(request):
    if request.user.is_superuser:
        admin = 'OK'
    else:
        admin = 'NO'
    if request.method == 'POST':
        form = WordForm(request.POST)
        find = request.POST['find']
        data = PrintModel.objects.filter(Q(title__contains=find)|Q(content__contains=find)|Q(author__username__contains=find)).order_by('id').reverse()
        c_num = PrintModel.objects.filter(Q(title__contains=find)|Q(content__contains=find)|Q(author__username__contains=find)).count()
        #data = PrintModel.objects.filter(title__contains=find).order_by('id').reverse()
    else:
        form = WordForm()
        data = PrintModel.objects.all().order_by('id').reverse()
        c_num = PrintModel.objects.all().count()
    context = {
        'form':form,
        'data':data,
        'admin':admin,
        'count':c_num
    }
    return render(request, 'printapp/find.html',context)







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

def Delete(request,pk):
    model = PrintModel.objects.get(id=pk)
    if request.method == 'POST':
        model.delete()
        return redirect('printapp:list')
    content = {
        'id':pk,
        'item':model
    }
    return render(request,'printapp/delete.html',content)




def commentDelete(request,pk):
    model = Comment.objects.get(id=pk)
    if request.method == 'POST':
        model.delete()
        return redirect('printapp:detail',pk=model.target.id)
    content = {
        'id':pk,
        'comments':model
    }
    return render(request,'printapp/deletecomment.html',content)





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


class CommentCreate(CreateView):
    """コメント投稿ページのビュー"""
    template_name = 'printapp/comment_form.html'
    model = Comment
    form_class = CommentCreateForm
 
    def form_valid(self, form):
        post_pk = self.kwargs['pk']
        post = get_object_or_404(PrintModel, pk=post_pk)
        comment = form.save(commit=False)
        comment.target = post
        form.instance.name = self.request.user
        comment.save()
        return redirect('printapp:detail', pk=post_pk)
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(PrintModel, pk=self.kwargs['pk'])
        return context



@login_required
def detailview(request,pk):
    object = PrintModel.objects.get(pk=pk)
    comment = Comment.objects.filter(target=object)

    return render(request, 'printapp/detail.html', {'object':object,'comment':comment})