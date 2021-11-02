from django.urls import path
from .views import user_profile,Profile_editview

app_name = 'accounts'

urlpatterns = [
    path('profile/<str:username>/',user_profile, name='profile'),
    path('edit/', Profile_editview.as_view(), name='edit')
]