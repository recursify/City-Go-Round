# NOTE: Must import *, since Django looks for things here, e.g. handler500.
from django.conf.urls.defaults import *

urlpatterns = patterns('')

urlpatterns += patterns(
    'opentransit.views',
    url('^$', 'home', name='home'),
    url('^example_petition_form$', 'example_petition_form', name='example_petition_form'),
    url('^example_petition_success$', 'example_petition_success', name='example_petition_success'),
)
