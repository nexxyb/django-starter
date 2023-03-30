
from django.urls import path, re_path
from apps.pages import views

app_name='pages'

urlpatterns = [

    # The home page
    path('', views.IndexView.as_view(), name='pages'),
    
    
]
