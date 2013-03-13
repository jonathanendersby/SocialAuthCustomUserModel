from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'', include('social_auth.urls')),
    url(r'^$', TemplateView.as_view(template_name="pre.html")),
    url(r'^post$', TemplateView.as_view(template_name="post.html")),
    url(r'^error$', TemplateView.as_view(template_name="error.html")),
)
