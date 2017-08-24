from django.conf.urls import url

from . import views

app_name = "app1"
urlpatterns = [
    #url(r'^contact/$', views.contact_view, name="contact_view"),
    #url(r'^appinfo/$', views.appinfo_view, name="appinfo_view"),

    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

]
