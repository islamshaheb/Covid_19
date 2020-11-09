
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('account/', include('App_Login.urls')),
    path('covid/',include('App_Covid.urls')),
    path('map/', include('Map_Data.urls')),#new
    path('dash/',include('Dashboard.urls')),
    path('more/', include('More_Info.urls')),
    path('',views.Index, name='Index'),#kew jdi just site er nam likhe tahole eta execute hbe
    #path('dash/',include('DashBoard.urls')),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
