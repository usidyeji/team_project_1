from django.forms import ModelForm
from .models import CountryData

class CountryDataForm(ModelForm):
  class Meta:
    model = CountryData
    # feilds = ['country', 'population'] # 이거를 한 꺼번에 가져온다는 게 아래 것
    fields = '__all__'