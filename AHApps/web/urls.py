from django.urls import path
from .views import *

urlpatterns = [
    path('', login_view, name='login_view'),
    path('new-register/', register_view, name='register_view'),
    path('logout/', logout, name='logout'),
    path('forgot-password/', forgot_password_view, name='forgot_password_view'),
    path('password-reset-request/', password_reset_request, name='password_reset_request'),
    path('dashboard/', dashboard_view, name='dashboard_view'),
    path('catalogue/', catalogue_view, name='catalogue_view'),
    path('profile/', profile_view, name='profile_view'),
    path('profile-update/', profile_update, name='profile_update'),
    path('forgot_password/', forgot_password_profile_view, name='forgot_password_profile_view'),
    path('update-date-of-birth/', update_date_of_birth, name='update_date_of_birth'),
    path('customer_care/', customer_care_view, name='customer_care_view'),
    path('edit-customer-request/', edit_customer_request, name="edit_customer_request"),
    path('delete-customer-request/<str:request_id>', delete_customer_request, name="delete_customer_request"),
    path('catalogue-details/<str:catalogue_id>', catalogue_details, name="catalogue_details"),
    path('catalogue/update/<str:catalog_id>', update_catalogue, name='update_catalogue'),
    path('news/', news_view, name='news'),
    path('update-mobile/', update_mobile_view, name='update_mobile'),
    ]