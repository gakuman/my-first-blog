from django import forms
from allauth.account.forms import SignupForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProfileForm(forms.Form):
    name = forms.CharField(max_length=25)
    icon = forms.ImageField(required=False)
    introduction = forms.CharField(max_length=75)
    

""" class SignupUserForm(SignupForm):
    username = forms.CharField(max_length=25,label='ユーザーネーム')

    def save(self, request):
        user = super(SignupUserForm, self).save(request)
        user.username = self.cleaned_data['username']
        user.save()
        return user """


class SignupUserForm(UserCreationForm):
    username = forms.CharField(
        max_length=25,
        help_text='オプション',
        label='ユーザーネーム'
    )

    email = forms.EmailField(
        max_length=254,
        help_text='必須:有効なメールアドレスを入力してください。',
        label='Eメールアドレス'
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )


class secretform(forms.Form):
    secret = forms.CharField(max_length=100, required=True)


class Findform(forms.Form):
    find = forms.fields.ChoiceField(
        choices=(
            ('全て','全て'),('japanese','国語'),('math','数学'),('english','英語'),('social_study','現代社会'),('chemistry','化学'),('biology','生物'),('physics','物理'),('other','その他')
        ),
        required=False,
        widget=forms.widgets.Select
    )