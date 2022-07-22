from django.urls import path
from core import views
from django.contrib.auth import views as auth_views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index),
    path('login/', views.login_page),
    path('login/submit', views.submit_log_in),

    path('signup/', views.registerUser),
    path('signup/submit', views.submit_signup),
    path('logout/', views.logout_user),

    path('post-categoria/', views.post_categoria),

    path('categorie/<int:id_categoria>', views.show_posts),
    path('post/<int:id_post>', views.post),

    path('perfil/<str:username>', views.perfil),

]


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
