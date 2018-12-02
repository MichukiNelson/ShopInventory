from django import forms

from .models import *

class DesktopForm(forms.ModelForm):
	class Meta:
		model = Desktop
		fields = [
			'name',
			'processor',
			'security',
			'ram',
			'storage',
			'status'
		]
		widgets = {'status': forms.Textarea(attrs={'cols': 80})}

class LaptopForm(forms.ModelForm):
	
	class Meta:
		model = Laptop
		fields = [
					'name',
					'processor',
					'security',
					'ram',
					'storage',
					'battery',
		 			'hdd_cover',
		 			'status'
		]
		hdd_cover = forms.ChoiceField(label="", initial='', 
		 widget=forms.Select(), required=True)
		battery = forms.ChoiceField(label="", initial='',
		 widget=forms.Select(), required=True)
		widgets = {'status': forms.Textarea(attrs={'cols': 80})}

class MonitorForm(forms.ModelForm):
	class Meta:
		model = Monitor
		fields = [
			'name',
			'size',
			'security',
			'resolution',
			'connectivity',
			'status'
		]
		widgets = {'status': forms.Textarea(attrs={'cols': 80})}

class GenericForm(forms.ModelForm):
	class Meta:
		model = Generic
		fields = ['item']
		widgets = {'item': forms.Textarea(attrs={'cols': 80})}
