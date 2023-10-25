from django.db import models
from users.models import User
from moment.models import Moment

class LikeOnMoment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    moment_id = models.ForeignKey(Moment, on_delete=models.CASCADE)
    pub_date = models.DateField(auto_now_add=True)