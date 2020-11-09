from django.urls import path
from More_Info import views
from django.conf.urls import url
app_name='More_Info'

urlpatterns=[
    path('show_more/', views.home, name='show_more'),
]
