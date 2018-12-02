from django.db import models

class CommonInfo(models.Model):
	"""Common fields inherited by models."""
	name = models.CharField(max_length=50)
	processor = models.CharField(max_length=30)
	security = models.CharField(max_length=100)
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		abstract = True

class Desktop(CommonInfo):
	"""Complete information about a specific Desktop."""
	ram = models.CharField(max_length=5)
	storage = models.CharField(max_length=10)
	status = models.TextField()

	def __str__(self):
		"""Return an string representation of the model."""
		return '%s %s %s %s %s %s' % (self.name, self.processor, self.security,
			self.ram, self.storage, self.status)
	
class Laptop(CommonInfo):
	"""Complete information about a specific laptop."""
	HDD_COVER = (
		('Cover Present', 'Present'),
		('Cover Absent', 'Absent'),
		)
	BATTERY = (
		('Battery Present', 'Present'),
		('Battery Absent', 'Absent'),
		)
	ram = models.CharField(max_length=5)
	storage = models.CharField(max_length=10)
	hdd_cover = models.CharField(max_length=15, choices=HDD_COVER,
		default='choose')
	battery = models.CharField(max_length=15, choices=BATTERY, default='choose')
	status = models.TextField()

	def __str__(self):
		"""Return an string representation of the model."""
		return '%s %s %s %s %s %s %s %s' % (self.name, self.processor, 
			self.security, self.ram, self.storage, self.hdd_cover,
			self.battery, self.status)

class Monitor(models.Model):
	"""Specific information about a monitor."""
	name = models.CharField(max_length=50)
	size = models.CharField(max_length=10)
	security = models.CharField(max_length=100)
	resolution = models.CharField(max_length=20)
	connectivity = models.CharField(max_length=50)
	status = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		"""Return an string representation of the model."""
		return '%s %s %s %s %s %s' % (self.name, self.size, self.security,
			self.resolution, self.connectivity, self.status,
			)

class Generic(models.Model):
	"""Allows entry of generic items."""
	item = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		"""Return a string representation of the entry."""
		return self.item


