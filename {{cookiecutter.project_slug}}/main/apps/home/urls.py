
from django.urls import path, re_path
from apps.home import views

app_name='home'

urlpatterns = [

    # The home page
    path('', views.IndexView.as_view(), name='home'),
    
    
]
