"""Defines URL patterns for inventory."""

from django.conf.urls import url

from . import views

urlpatterns = [
	# Home Page.
	url(r'^$', views.index, name='index'),
	# Add item page
	url(r'^add_item/$', views.add_item, name='add_item'),
	# Adding item to Desktop category.
	url(r'^add_item/desktop/$', views.add_desktop, name='add_desktop'),
	# Adding item to laptop category.
	url(r'^add_item/laptop/$', views.add_laptop, name='add_laptop'),
	# Adding item to Monitor category.
	url(r'^add_item/monitor/$', views.add_monitor, name='add_monitor'),
	# Adding item to generic page
	url(r'^add_item/generic_item/$',views.add_generic, name='add_generic'),
	# View inventory.
	url(r'^view_inventory/$', views.inventory, name='inventory'),
	# View Desktops
	url(r'^inventory/desktop/$', views.desktops, name='desktops'),
	# Edit desktop
	url(r'^edit_desktop/(?P<desktop_id>\d+)/$', views.edit_desktop, name='edit_desktop'),
	# View Laptops.
	url(r'^inventory/laptop/$', views.laptops, name='laptops'),
	# Edit laptop
	url(r'^edit_laptop/(?P<laptop_id>\d+)/$', views.edit_laptop, name='edit_laptop'),
	# View Monitors.
	url(r'^inventory/monitor/$', views.monitors, name='monitors'),
	# Edit monitor
	url(r'^edit_monitor/(?P<monitor_id>\d+)/$', views.edit_monitor, name='edit_monitor'),
	# Add Generic.
	url(r'^inventory/generic/$', views.generic, name='generic'),
	# Edit generic
	url(r'^edit_generic/(?P<generic_id>\d+)/$', views.edit_generic, name='edit_generic'),
]