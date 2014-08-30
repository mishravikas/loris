# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = patterns('',
	(r'^myapp/', include('myproject.myapp.urls')),
	(r'^$', RedirectView.as_view(url='/myapp/list/')),
	(r'^download/', 'myproject.myapp.views.output_download'),
	(r'^getfiles/', 'myproject.myapp.views.getfiles'),
	 # Just for ease of use.
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
