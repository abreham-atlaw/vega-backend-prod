from django.contrib.auth.models import BaseUserManager


class VegaUserManager(BaseUserManager):

	def create_user(self, full_name, email, password=None):
		if not email:
			raise ValueError('Users must have an email')

		user = self.model(
			full_name=full_name,
			email=email,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, password, full_name):
		user = self.create_user(
			email=email,
			password=password,
			full_name=full_name
		)
		user.is_admin = True
		user.save(using=self._db)
		return user

