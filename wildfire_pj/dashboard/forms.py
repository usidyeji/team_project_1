from django.forms import ModelForm
from .models import Wildfire

class WildfireDataForm(ModelForm):
  class Meta:
    model = Wildfire
    # feilds = ['country', 'population'] # 이거를 한 꺼번에 가져온다는 게 아래 것
    fields = '__all__'