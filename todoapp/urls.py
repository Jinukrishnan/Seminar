
from django.urls import path
from . import views
app_name='todo'
urlpatterns = [
    
    path('',views.Home,name='home'),
    path('/delete/<int:id>',views.Delete,name='delete'),
    path('/update/<int:id>',views.Update,name='update'),
]