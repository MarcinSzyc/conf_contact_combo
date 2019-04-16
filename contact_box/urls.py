"""warsztat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from contact_box.views import \
    PersonAll, NewPerson, ModifyPersonView, DeletePerson, \
    NewEmail, NewAddress, NewPhoneNumber, NewGroup, DeletePhone, DeleteEmail
# DeleteGroup, ,
app_name = "contact_box"

urlpatterns = [
    path('', PersonAll.as_view(), name='person_all'),
    path('new/', NewPerson.as_view(), name='new_person'),
    path('modify/<int:id>', ModifyPersonView.as_view(), name='modify_person_view'),
    path('delete/<int:id>', DeletePerson.as_view(), name='delete_person'),
    path('new_email/', NewEmail.as_view(), name='new_email'),
    path('new_address/', NewAddress.as_view(), name='new_address'),
    path('new_phone_number/', NewPhoneNumber.as_view(), name='new_phone_number'),
    path('new_group/', NewGroup.as_view(), name='new_group'),
    # path('delete_group/', DeleteGroup.as_view(), name='delete_group'),
    path('delete_phone/<int:id>', DeletePhone.as_view(), name='delete_phone'),
    path('delete_email/<int:id>', DeleteEmail.as_view(), name='delete_email'),
]
