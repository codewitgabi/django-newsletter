from django.db import models
import uuid


class Subscriber(models.Model):
	""" Subscribers Table """
	id = models.UUIDField(
		default=uuid.uuid4,
		editable=False,
		primary_key=True
	)
	email = models.EmailField(unique= True)
	
	def __str__(self):
		return self.email


class Message(models.Model):
	""" Message to send to subscribers """
	id = models.UUIDField(
		default=uuid.uuid4,
		editable=False,
		primary_key=True
	)
	message = models.TextField()
	scheduled_time = models.DateTimeField()
	sent = models.BooleanField(default=False)
	
	def __str__(self):
		return self.message

