from django.conf.urls import url

from . import views

app_name = 'app1'
urlpatterns = [
    url(r'^$', views.main_view, name="main_view"),
    url(r'^contact/$', views.contact_view, name="contact_view"),
    url(r'^appinfo/$', views.appinfo_view, name="appinfo_view"),

    url(r'^details/(?P<question_id>[0-9]+)/$', views.detail_view, name="detail_view"),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results_view, name="results_view"),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote_view, name="vote_view"),


]
