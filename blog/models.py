from django.db import models
from django.utils.timezone import now
from account.models import User


class Article(models.Model):
    title = models.CharField(max_length=500)
    caption = models.TextField()
    image = models.FileField(upload_to='blog/image')
    is_public = models.BooleanField(default=True)
    is_special = models.BooleanField(default=False)
    publisher = models.ForeignKey(User , on_delete=models.CASCADE , related_name='articles')
    date_added = models.DateField(default=now)

    def __str__(self) -> str:
        return self.title
