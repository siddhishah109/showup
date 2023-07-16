from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def certificate_image_upload_path(instance, filename):
    # return f'certificates/{instance.user.id}/{filename}'
     return f'certificates/{filename}'


class Certificate(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to=certificate_image_upload_path)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    # Add any other fields specific to your certificates

    def __str__(self):
        return self.title

