from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Custom(models.Model):
    name = models.CharField(max_length=50)

class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="uploads",null=True,blank=True)
    email = models.EmailField(max_length=255,unique=True,null=True)
    phone = models.CharField(max_length=20,blank=True,null=True)
    gender = models.CharField(max_length=10,blank=True,null=True)

    REQUIRED_FIELDS = []
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        return f"User: {self.username} Email: {self.email}"