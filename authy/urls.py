from django.urls import path
from .views import user_logout,user_register,user_login,follow,unfollow,profile,edit_profile

app_name = 'accounts'


urlpatterns = [
    path('register/', user_register, name='user_register'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('follow/<str:username>', follow, name='follow'),
    path('unfollow/<str:username>', unfollow, name='unfollow'),
    path('<str:username>/_saved/', profile, name='profile'),
    path('settings/edit-profile/', edit_profile, name='edit_profile'),
]