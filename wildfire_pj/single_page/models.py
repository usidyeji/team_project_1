from django.db import models

# Create your models here.
class Resume(models.Model):
  file_upload = models.FileField(upload_to='classnote/files/%Y/%m/%d/', blank=True)
