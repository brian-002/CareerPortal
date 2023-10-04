from django.urls import path

from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'customercare'

urlpatterns = [
    path('', views.inbox, name= 'inbox'),
    path('<int:pk>/', views.detail, name= 'detail'),
    path('new/<int:item_pk>/', views.new_conversation, name='new'),
    
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)







