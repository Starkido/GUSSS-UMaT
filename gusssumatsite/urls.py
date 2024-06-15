# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('member/dashboard/', views.member_dashboard, name='member_dashboard'),
#     path('finance/officer/dashboard/', views.finance_officer_dashboard, name='finance_officer_dashboard'),
#     # Add more URL patterns as needed
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.loginUser, name='login'),
    path('do_login/', views.doLogin, name='do_login'),
    path('member/dashboard/', views.member_dashboard, name='member_dashboard'),
    path('finance/officer/dashboard/', views.finance_officer_dashboard, name='finance_officer_dashboard'),
    # Add more URL patterns as needed
]
