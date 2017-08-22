from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.main_view, name="main_view"),
    url(r'^contact/$', views.contact_view, name="contact_view"),
    url(r'^appinfo/$', views.appinfo_view, name="appinfo_view"),
    #url(r'^appinfo/$', views.appinfo_view, name="appinfo_view"),

]
