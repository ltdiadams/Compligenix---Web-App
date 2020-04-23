"""quotemobile URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
# from django.urls import path
# # from main.views import first
# from . import views
#
# urlpatterns = [
#     # path('', insert_my_num),
#     # path('index/', ),
#     path('insert_num/', views.insert_my_num,name='insert_my_num')
# ]

from django.urls import path
from . import views

urlpatterns =[
    path('list/',views.list_phone_items),
    path('insert_phone/',views.insert_phone_item,name='insert_phone_item'),
    path('delete_phone/<int:phone_id>/',views.delete_phone_item,name='delete_phone_item'),
]

