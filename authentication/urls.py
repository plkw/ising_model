from django.conf.urls import url

from django.views.generic import TemplateView
from . import views

urlpatterns = [

    url(r'^$', TemplateView.as_view(template_name='authentication/index.html')),
    url(r'^register/$', views.RegisterFormView.as_view()),
    url(r'^login/$', views.LoginFormView.as_view()),
    url(r'^logout/$', views.LogoutView.as_view()),
]