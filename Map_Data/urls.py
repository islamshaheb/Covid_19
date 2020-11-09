from django.urls import path
from Map_Data import views
from django.conf.urls import url
app_name='Map_Data'

urlpatterns=[
    path('show_map/', views.index, name='show_map'),
    url('selectCountry',views.drillDownACountry,name='drillDown'),
]
