from .import views
from django.urls import path

app_name = 'education'

urlpatterns = [ 
    path('', views.welcome_page, name='welcome_page'),
    path('index', views.index, name='index'),
    path('<int:resource_id>/', views.detail,name = 'detail'),
    path('add', views.add_feedback, name="add_feedback"),
   
    ]
    
