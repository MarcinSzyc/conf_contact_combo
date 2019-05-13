from django.urls import path, re_path
from general.views import Home
from general.views import Login, Logout, Register
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', Home.as_view(), name="Home"),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('register/', Register.as_view(), name='register'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>',
            auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/completed/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
