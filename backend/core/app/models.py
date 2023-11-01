from django.db import models

# Create your models here.
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
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = UserAccountManager()

    photo_path = models.CharField(max_length=300, verbose_name="Путь до фото", null=True)
    rating = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Рейтинг", null=True)

class Comment(models.Model):
    content = models.TextField(max_length=5000)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

class Moment(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(max_length=5000)#is_deleted сделать
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateField(auto_now_add=True)
    photo_path = models.CharField(max_length=300, verbose_name="Путь до фото", null=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class LikeOnComment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE)
    pub_date = models.DateField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

class LikeOnMoment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    moment_id = models.ForeignKey(Moment, on_delete=models.CASCADE)
    pub_date = models.DateField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

class Subscrition(models.Model):
    subscriber_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriber')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,related_name='author')
    pub_date = models.DateField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

class Tag(models.Model):
    title = models.CharField(max_length=50)
    moment_id = models.ForeignKey(Moment, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)