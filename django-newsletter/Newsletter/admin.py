from django.contrib import admin
from .models import Subscriber, Message


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
	list_display = ("email",)
	search_fields = ("id", "email")


@admin.register(Message)
class SubscriptionMessageAdmin(admin.ModelAdmin):
	list_display = ("message", "scheduled_time", "sent")
	
