from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager

#Пользователь – электронная почта, никнейм, пароль, аватарка, дата регистрации, рейтинг.

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

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

    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
    rating = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Рейтинг", null=True)


class MomentsManager(models.Manager):
    def get_my_moments(self, pk):
        return Moment.objects.filter(user_id=pk, is_deleted = False).order_by('-pub_date')
    def get_all(self):
        return Moment.objects.filter(is_deleted = False).order_by('-pub_date')
    def get_subscriptions(self, sub_users):
        return Moment.objects.filter(user_id__in=sub_users, is_deleted = False).order_by('-pub_date')
    def get_count(self, pk):
        return Moment.objects.filter(user_id = pk).count()

class Moment(models.Model):
    objects = MomentsManager()

    title = models.CharField(max_length=150)
    content = models.TextField(max_length=5000)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateField(auto_now_add=True)
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.TextField(max_length=5000)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    moment_id = models.ForeignKey(Moment, on_delete=models.CASCADE)
    pub_date = models.DateField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

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

class Test(models.Model):
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
