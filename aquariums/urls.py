from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from aquariums.models import Aquarium

urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(
            queryset=Aquarium.objects.order_by('created_date')[:5],
            context_object_name='aquarium_list',
            template_name='aquariums/index.html'),
        name='index'),
    #aquarium detailed view with respective analyses:
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Aquarium,
            template_name='aquariums/detail.html'),
        name='detail'),
    #add a new aquarium:
    url(r'^new/$', 'aquariums.views.new', name='new'),
    #add a new analysis:
    url(r'^(?P<aquarium_id>\d+)/analysis/$', 'aquariums.views.analysis', name='analysis'),
    #add a fish:
    url(r'^(?P<aquarium_id>\d+)/fish/$', 'aquariums.views.fish', name='fish'),
)

