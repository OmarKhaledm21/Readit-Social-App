from django.db import models
from app.user.models import User
from app.community.models import Community

from django.core.validators import MinLengthValidator
from django.urls import reverse
# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f"{self.caption}"
        
class Post(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="posts", null=True,blank=True)
    date = models.DateField(auto_now=True, auto_now_add=False)
    slug = models.SlugField(unique=True, null=False)

    content = models.TextField(validators=[MinLengthValidator(10)])

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name="posts")

    community = models.ForeignKey(Community, on_delete=models.CASCADE,related_name="posts",null=True)

    tags = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return f"Title: {self.title}, Date = {self.date}, Slug: {self.slug}, Community: {self.community.community_name}"

    def get_absolute_url(self):
        return reverse("post-detail-page", args=[self.slug])
    class Meta:
        ordering = ['date']


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

    text = models.TextField(max_length=400)

    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, null=True)
