from django.db import models
from django.db.models.query import QuerySet


class AddressBookUserQuerySet(QuerySet):
	def active(self):
		return self.filter(is_active=True)

	def by_user(self, user_id):
		return self.filter(added_by=user_id)


class AddressBookUser(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20, blank=True, null=True)
	phone = models.CharField(max_length=15, blank=True, null=True, unique=True)
	email = models.EmailField(blank=True, null=True, unique=True)
	added_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	is_active = models.BooleanField(default=True)

	objects = AddressBookUserQuerySet.as_manager()

	class Meta:
		ordering = ['-created_at']

	def mark_inactive(self):
		self.is_active = False
