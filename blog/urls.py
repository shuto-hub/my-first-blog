from django.contrib.auth import views as auth_views
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/mypage/', views.mypage, name='mypage'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/',include('accounts.urls')),
]