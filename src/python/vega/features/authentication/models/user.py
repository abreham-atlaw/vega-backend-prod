from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from features.authentication.managers import VegaUserManager


class VegaUser(AbstractBaseUser):
	USERNAME_FIELD = 'email'

	full_name = models.CharField(max_length=64)
	email = models.CharField(
		verbose_name='Email',
		max_length=255,
		unique=True,
	)
	is_verified = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)

	objects = VegaUserManager()

	def __str__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
		return True

	@property
	def is_staff(self):
		return self.is_admin


class Verification(models.Model):
	user = models.ForeignKey(VegaUser, on_delete=models.CASCADE)
	key = models.CharField(max_length=16)
	creation_date_time = models.DateTimeField(auto_now_add=True)
