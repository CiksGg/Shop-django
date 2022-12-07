from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True


    def _create(self, email, password, **kwargs):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        #self.model=User
        user = self.model(email=email, **kwargs)
        user.set_password(password) # хеширует парль
        user.save(using=self._db) #сохраняем в бд
        return user


    def create_user(self, email, password, **kwargs):
        return self._create(email, password, **kwargs)


    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)
        return self._create(email, password, **kwargs)


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username= None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()