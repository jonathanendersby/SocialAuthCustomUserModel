from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class UserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, first_name=None, last_name=None, **extra_fields):
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            username=username,
            email=UserManager.normalize_email(email),
            first_name=first_name or '',
            last_name=last_name or '',
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, first_name=None, last_name=None):
        user = self.create_user(
            username,
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=254, unique=True, db_index=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)


    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.first_name

    def is_staff(self):
        return self.is_admin

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class Post(models.Model):
    user = User
    post = models.TextField()
