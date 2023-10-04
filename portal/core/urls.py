from django.urls import path

from django.contrib.auth import views as auth_views

from django.contrib.auth.views import LogoutView

from . import views

from .forms import LoginForm

from django.conf import settings
from django.conf.urls.static import static



app_name='core'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('user profile/', views.userprofile, name='userprofile'),
    path('about/', views.about, name='about'),
    path('Terms Of Use/', views.termofuse, name='termofuse'),
    path('Privacy policy/', views.privacyPolicy, name='privacyPolicy'),
    path('signup/', views.signup, name='signup'),
    path('my basket/', views.myBasket, name='myBasket'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view( template_name = 'core/login.html', authentication_form = LoginForm), name='login'),
    path('create-profile/', views.create_user_profile, name='create_user_profile'),
    path('edit-profile/', views.edit_user_profile, name='edit_user_profile'),
    path('apply for job/', views.apply_for_job, name='apply_for_job'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)