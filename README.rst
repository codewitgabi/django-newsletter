=================
django-newsletter
=================

This package is for automatically sending mails to subscribers.

Quick Start
-------------

1. Add "newsletter" to INSTALLED_APPS in your project's settings.py
   INSTALLED_APPS = [
       ....
       "newsletter",
       ....
   ]

2. Do your default django email customization.

3. add "SUBSCRIPTION_SUBJECT" in settings.py

4. Run ``python manage.py migrate`` on your command prompt or terminal to create the newsletter table.

5. Start the server and head over to the admin to add subscribers and messages.

