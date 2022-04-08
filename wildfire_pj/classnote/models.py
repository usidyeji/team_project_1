from django.db import models

# Create your models here.

### 노트 작성란
class Post(models.Model):
  title = models.CharField(max_length=40)
  hook_text = models.CharField(max_length=100, blank=True)
  content = models.TextField()

  created_at = models.DateTimeField(auto_now_add=True) # DB에 시간 자동으로 들어가게
  updated_at = models.DateTimeField(auto_now=True) # DB에 업데이트 시 시간 자동으로 들어가게

  def __str__(self):
    return f'[{self.pk}] {self.title}'  
    # return f'[{self.pk}] {self.title} :: {self.author}'  

  def get_absolute_url(self):
    return f'/note/{self.pk}/'