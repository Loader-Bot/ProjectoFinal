from django.db import models
from django.contrib.auth.models import User
from .utils import validate_image_file_extension, max_file_size


class NewsPost(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='posts_images', null=True, blank=True, validators=[validate_image_file_extension, max_file_size])
    created_at = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
       return self.title
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.user.username


class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return f"{self.user}"
    