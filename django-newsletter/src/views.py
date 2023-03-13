""" Django Imports """
from django.shortcuts import render
from django.utils.timesince import timeuntil, timesince
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings

""" Custom Imports """
from .models import Subscriber, Message

""" builtin Imports """
import time
from sys import stdout
import socket


def send_subscription_message() -> None:
	"""
	Creates a thread to send messages in `SubscriptionMessage` to members of a given `Subscription`.
	Subscribers are related to the currently used `User` model therefore, every user is expected to have their email ready.
	"""
	
	def broadcast_mail(message: str) -> int:
		"""
		Mail sending handler
		"""
		subscribers = Subscriber.objects.all()
		
		email = EmailMessage(
			settings.SUBSCRIPTION_SUBJECT,
			render_to_string("src/mail.html", {"message": message}),
			to = [subscriber.email for subscriber in subscribers]
		)
		
		email.content_subtype = "html"
		email.fail_silently = False
		email.send()
		
		return 0
		
	
	while True:
		time.sleep(1)
		
		# get all subscriptions
		subscriptions = Subscriber.objects.all()
		sub_messages = Message.objects.filter(sent=False)
	
		for message in sub_messages:
			try:
				hour, is_hour = timeuntil(message.scheduled_time).split(", ")[-2].split("\xa0")
			except IndexError:
				hour = "0"
				is_hour = "hours"
			
			mins, is_mins = timeuntil(message.scheduled_time).split(", ")[-1].split("\xa0")
			
			if (mins == "0" and is_mins == "minutes") and \
			(hour == "0" and is_hour == "hours"):
				
				# send mail
				try:
					broadcast_mail(message.message)
					# mark message as sent
					message.sent = True
					message.save()
					
					stdout.write(f"[INFO] {message.id} [STATUS] Sent\n")
		
				except socket.gaierror:
					print("An error occurred!!!")
				
				