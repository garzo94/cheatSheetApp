from django.urls import path
from . import views

app_name = 'cheatApp'


urlpatterns = [
    path('',  views.home_view, name='home_view'),
    path('mySheets/', views.mySheets, name='mySheets')
]