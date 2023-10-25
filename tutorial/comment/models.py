from django.db import models
from users.models import User

class Comment(models.Model):
    content = models.TextField(max_length=5000)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateField(auto_now_add=True)

#Все в одно приложение засунуть модели и сериалайзеры
#core и app
