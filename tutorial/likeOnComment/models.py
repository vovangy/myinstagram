from django.db import models
from users.models import User
from comment.models import Comment

class LikeOnComment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE)
    pub_date = models.DateField(auto_now_add=True)
    #generic for in key посмотреть https://docs.djangoproject.com/en/4.2/ref/contrib/contenttypes/