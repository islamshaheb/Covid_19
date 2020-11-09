from django.urls import path
from Dashboard import views
from django.conf.urls import url
app_name='Dashboard'

urlpatterns=[
    path('show_dash/', views.index, name='show_dash'),
]
