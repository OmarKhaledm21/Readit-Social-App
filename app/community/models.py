from distutils.command.upload import upload
from django.db import models
from app.user.models import User
# Create your models here.


class Community(models.Model):
    community_name = models.CharField(max_length=30,unique=True,null=False)
    image = models.ImageField(upload_to="community_uploads",null=True)
    description = models.CharField(max_length=500,null=True)

    def __str__(self):
        return f"Community name: {self.community_name}"

    class Meta:
        verbose_name = 'Community'
        verbose_name_plural = 'Communities'
        

class UserCommunity(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    community = models.ForeignKey(Community,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f"{self.user} {self.community}"

    class Meta:
        verbose_name_plural = 'UserCommunity'