from . import views
from django.urls import path
from .views import *
from AHApps.web.views import login_view,register_view


urlpatterns = [
    path('',home,name='home'),
    path('base/', base, name='base'),
    path('catalogue/<str:catalogue_id>/', catalogue_detail, name='catalogue_detail'),
    path('login/', login_view, name='login_view'),
    path('new-register/', register_view, name='register_view'),

]