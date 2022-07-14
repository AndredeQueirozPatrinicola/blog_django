from django.urls import path
from core import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index),
    path('login/', views.login_page),
    path('login/submit', views.submit_log_in),

    path('signup/', views.registerUser),
    path('signup/submit', views.submit_signup),
    path('logout/', views.logout_user),

    path('post-categoria/', views.post_categoria),

#    path('categoria/<int:id_categoria>', views.categoria),

    path('post/', views.post)
]

