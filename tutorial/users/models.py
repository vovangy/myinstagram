from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager

#Пользователь – электронная почта, никнейм, пароль, аватарка, дата регистрации, рейтинг.

class UserAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Почта обязательна для регистрации")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, email, username,  password=None):
        if not email:
            raise ValueError("Почта обязательна для регистрации")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username)
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user

class User(AbstractUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)#
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = UserAccountManager()

    photo_path = models.CharField(max_length=300, verbose_name="Путь до фото", null=True)
    rating = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Рейтинг", null=True)

#class User(models.Model):
    #company_name = models.CharField(max_length=50, verbose_name="Название компании")
    #price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Цена акции")
    #is_growing = models.BooleanField(verbose_name="Растет ли акция в цене?")
    #date_modified = models.DateTimeField(auto_now=True, verbose_name="Когда последний раз обновлялось значение акции?")