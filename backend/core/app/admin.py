from django.contrib import admin
from app.models import User, Moment, Comment, LikeOnComment, LikeOnMoment, Tag, Subscrition, Test

admin.site.register(User)
admin.site.register(Moment)
admin.site.register(Comment)
admin.site.register(LikeOnMoment)
admin.site.register(LikeOnComment)
admin.site.register(Tag)
admin.site.register(Subscrition)
admin.site.register(Test)

# Register your models here.
