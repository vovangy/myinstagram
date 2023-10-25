from django.db import models
from users.models import User

class Moment(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(max_length=5000)#is_deleted сделать
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateField(auto_now_add=True)
    photo_path = models.CharField(max_length=300, verbose_name="Путь до фото", null=True)

    def __str__(self):
        return self.title
