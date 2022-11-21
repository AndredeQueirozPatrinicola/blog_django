from django.urls import path, include, re_path
from core import views
from django.contrib.auth import views as auth_views


from django.conf.urls.static import static
from django.views.static import serve
from django.conf import settings

app_name = 'core'

urlpatterns = [
    path('', views.index),
    path('login/', views.login_page),
    path('login/submit', views.submit_log_in),

    path('signup/', views.registerUser),
    path('signup/submit', views.submit_signup),
    path('logout/', views.logout_user),

    path('post-categoria/', views.post_categoria),
    path('post-design/', views.post_design),
    path('categorie-design/', views.categorie_design),
    path('post-design/submit', views.submit_post),
    path('categorie-design/submit', views.submit_categoria),

    path('categorie/<int:id_categoria>', views.show_posts),
    path('post/<int:id_post>', views.post),

    path('perfil/<str:id_user>', views.perfil),
    path('perfil/<int:id_user>/submit', views.submit_edicao),
    path('perfil/<int:id_user>/submit_imagem', views.submit_imagem),
    path('perfil/<str:id_user>/editar-perfil', views.editar_perfil),
    path('perfil/<str:id_user>/editar-imagem', views.editar_imagem),    


    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
