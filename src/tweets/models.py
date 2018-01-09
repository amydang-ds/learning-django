from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.


def get_sentinel_user():
	return get_user_model().objects.get_or_create(username='deleted')[0]

class Tweet(models.Model):
	user = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.SET(get_sentinel_user),
		)
	content 	= models.CharField(max_length=140)
	updated		= models.DateTimeField(auto_now=True)
	timestamp	= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.content)
