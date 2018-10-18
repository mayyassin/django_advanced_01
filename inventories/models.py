from django.db import models
from django.contrib.auth.models import User
from stores.models import Store

# Create your models here.
class Inventory(models.Model): 
	name = models.TextField()
	store = models.ForeignKey(Store, default=1, on_delete=models.CASCADE)
	Y = 'Yes'
	N = 'No'
	EMPTY_CHOICES = ((Y, 'Yes'), (N, 'No'))
	is_empty = models.CharField(max_length=10, choices=EMPTY_CHOICES, default='1')
	last_updated = models.DateTimeField()

	
