from django.db import models
from django.db.models.query import QuerySet

from address.choices import AddressType

class AddressQuerySet(QuerySet):
	def active(self):
		return self.filter(is_active=True, user__is_active=True)

	def by_user(self, user_id):
		return self.filter(added_by_id=user_id)

class AddressEntry(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	user = models.ForeignKey('user.AddressBookUser', on_delete=models.CASCADE)
	line1 = models.CharField(max_length=20)
	line2 = models.CharField(max_length=20, blank=True, null=True)
	city = models.CharField(max_length=20)
	state = models.CharField(max_length=20)
	country = models.CharField(max_length=20)
	pincode = models.CharField(max_length=10) # some countries have alphanumeric pincodes
	type = models.CharField(choices=AddressType.choices, max_length=16, blank=True, null=True)
	added_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	is_active = models.BooleanField(default=True) # set to False if the address is deleted

	objects = AddressQuerySet.as_manager()

	class Meta:
		ordering = ['-created_at']

	def mark_inactive(self):
		self.is_active = False

