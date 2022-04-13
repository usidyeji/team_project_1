from django.shortcuts import redirect, render
from .models import Wildfire

# Create your views here.
def dashboard(request):
  # 각 나라와 인구 수 가져오기
  data = Wildfire.objects.all()
  # print(data)
  return render(request, 'dashboard/dashboard.html',)


  # class CountryData(models.Model):
  # country = models.CharField(max_length=100)
  # population = models.IntegerField()
