from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from mainapp.views import index, signup, list, create_build, completed_builds, build_detail

urlpatterns = [
    path('', index, name="index"),
    path('login/', auth_views.LoginView.as_view(template_name='mainapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', signup, name="signup"),
    path('list/', list, name="list"),
    path("create-build/", create_build, name="create_build"),
    path('completed-builds/', completed_builds, name='completed_builds'),
    path('build/<int:build_id>/', build_detail, name='build_detail'),
]