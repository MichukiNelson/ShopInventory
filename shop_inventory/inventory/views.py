from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *

def index(request):
	"""The home page for inventory."""
	return render(request, 'inventory/index.html')

@login_required
def add_item(request):
	"""The add item page."""
	return render(request, 'inventory/add_item.html')

@login_required
def inventory(request):
	"""Inventory page."""
	return render(request, 'inventory/inventory.html')

@login_required
def add_desktop(request):
	"""Add a new desktop."""
	if request.method != 'POST':
		# Create an empty form
		form = DesktopForm()
	else:
		# Post and process the data entered.
		form = DesktopForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('inventory:desktops'))

	context = {'form': form}

	return render(request, 'inventory/add_desktop.html', context)

@login_required
def add_laptop(request):
	"""Add a new laptop."""
	if request.method != 'POST':
		# Create an empty form
		form = LaptopForm()
	else:
		# Post and process the data entered.
		form = LaptopForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('inventory:laptops'))

	context = {'form': form}

	return render(request, 'inventory/add_laptop.html', context)

@login_required
def add_monitor(request):
	"""Add new monitor."""
	if request.method != 'POST':
		# Create an empty form
		form = MonitorForm()
	else:
		# Post and process the data entered.
		form = MonitorForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('inventory:monitors'))

	context = {'form': form}

	return render(request, 'inventory/add_monitor.html', context)

@login_required
def add_generic(request):
	"""Add a non-specific item."""
	if request.method != 'POST':
		# Create an empty form
		form = GenericForm()
	else:
		# Post and process the data entered.
		form = GenericForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('inventory:generic'))

	context = {'form': form}

	return render(request, 'inventory/add_generic.html', context)	

@login_required
def desktops(request):
	"""View desktops in inventory."""
	items = Desktop.objects.all()
	desktops = items.order_by('date_added')
	context = {'desktops': desktops}
	return render(request, 'inventory/desktops.html', context)

@login_required
def edit_desktop(request, desktop_id):
	"""Edit specific desktop entry."""
	desktop = Desktop.objects.get(id=desktop_id)

	if request.method != 'POST':
		# Initial request; pre-fill form with the current desktop.
		form = DesktopForm(instance=desktop)
	else:
		# Post data submited, process data.
		form = DesktopForm(instance=desktop, data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('inventory:desktops'))

	context = {'desktop': desktop, 'form': form}
	return render(request, 'inventory/edit_desktop.html', context)

@login_required
def laptops(request):
	"""View laptops in inventory."""
	items = Laptop.objects.all()
	laptops = items.order_by('date_added')
	context = {'laptops': laptops}
	return render(request, 'inventory/laptops.html', context)

@login_required
def edit_laptop(request, laptop_id):
	"""Edit specific laptop entry."""
	laptop = Laptop.objects.get(id=laptop_id)

	if request.method != 'POST':
		# Initial request; pre-fill form with the current laptop.
		form = LaptopForm(instance=laptop)
	else:
		# Post data submited, process data.
		form = LaptopForm(instance=laptop, data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('inventory:laptops'))

	context = {'laptop': laptop, 'form': form}
	return render(request, 'inventory/edit_laptop.html', context)

@login_required
def monitors(request):
	"""View monitors in inventory."""
	# monitors = serializers.serialize('python', Monitor.objects.all())
	items = Monitor.objects.all()
	monitors = items.order_by('date_added')
	context = {'monitors': monitors}
	return render(request, 'inventory/monitors.html', context)

@login_required
def edit_monitor(request, monitor_id):
	"""Edit specific monitor entry."""
	monitor = Monitor.objects.get(id=monitor_id)

	if request.method != 'POST':
		# Initial request; pre-fill form with the current monitor.
		form = MonitorForm(instance=monitor)
	else:
		# Post data submited, process data.
		form = MonitorForm(instance=monitor, data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('inventory:monitors'))

	context = {'monitor': monitor, 'form': form}
	return render(request, 'inventory/edit_monitor.html', context)

@login_required
def generic(request):
	"""View generic in inventory."""
	items = Generic.objects.all()
	generics = items.order_by('date_added')
	context = {'generics': generics}
	return render(request, 'inventory/generic.html', context)

@login_required
def edit_generic(request, generic_id):
	"""Edit specific generic entry."""
	generic = Generic.objects.get(id=generic_id)

	if request.method != 'POST':
		# Initial request; pre-fill form with the current generic.
		form = GenericForm(instance=generic)
	else:
		# Post data submited, process data.
		form = GenericForm(instance=generic, data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('inventory:generic'))

	context = {'generic': generic, 'form': form}
	return render(request, 'inventory/edit_generic.html', context)
