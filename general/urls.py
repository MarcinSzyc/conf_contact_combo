from django.urls import path
from general.views import Home
from general.views import Login, Logout


urlpatterns = [
    path('', Home.as_view(), name="Home"),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
]