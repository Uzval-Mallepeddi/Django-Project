from django.conf.urls import url
from myportfolio import views

app_name = 'myportfolio'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home/$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^projects/$', views.projects, name='projects'),
    url(r'^skills/$', views.skills, name='skills'),
    url(r'^newproject/$', views.project_form, name='projectform')
]
