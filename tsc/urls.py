from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
import views

###############################################################################
urlpatterns = patterns('tsc',
        url(r'^add/(?P<login_key>[\w-]+)$',
        views.add,
        name="tsc_add"),

        url(r'^add/$',
        views.add,
        name="tsc_add"),

        url(r'^test$',
            direct_to_template,
            {'template':'tsc_test.html'},
            name="tsc_test"),
)
