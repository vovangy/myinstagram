from django.db import models
from users.models import User

class Subscrition(models.Model):
    subscriber_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriber')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,related_name='author')
    pub_date = models.DateField(auto_now_add=True)
