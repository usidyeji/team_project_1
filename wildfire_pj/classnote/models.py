from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
from markdownx.utils import markdown
import os

# Create your models here.

### Tag
class Tag(models.Model):
  name = models.CharField(max_length=50)
  slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

  def __str__(self):
      return self.name

  def get_absolute_url(self):
      return f'/note/tag/{self.slug}/'

### 노트 작성란
class Post(models.Model):
  title = models.CharField(max_length=40)
  hook_text = models.CharField(max_length=100, blank=True)
  content = MarkdownxField()

  file_upload = models.FileField(upload_to='classnote/files/%Y/%m/%d/', blank=True)

  created_at = models.DateTimeField(auto_now_add=True) # DB에 시간 자동으로 들어가게
  updated_at = models.DateTimeField(auto_now=True) # DB에 업데이트 시 시간 자동으로 들어가게

  author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
  tags = models.ManyToManyField(Tag, blank=True)


  def __str__(self):
    return f'[{self.pk}] {self.title}'  
    # return f'[{self.pk}] {self.title} :: {self.author}'  

  def get_absolute_url(self):
    return f'/note/{self.pk}/'

  def get_file_name(self):
    return os.path.basename(self.file_upload.name)

  def get_file_ext(self):
    return self.get_file_name().spilt('.')[-1]

  def get_content_markdown(self):
    return markdown(self.content)
