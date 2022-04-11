from django.shortcuts import redirect, render
from .models import CountryData
from .forms import CountryDataForm

# Create your views here.
def dashboard(request):
  # 각 나라와 인구 수 가져오기
  data = CountryData.objects.all()
  # print(data)

  # add 버튼 클릭, 값 입력 요청 처리
  if request.method == 'POST':
    # DB 입력
    form = CountryDataForm(request.POST)

    if form.is_valid():
      # DB에 나라 이름 중복될 경우, 인구 수 업데이트 / 아닌 경우 추가
      #CRUD : Create, Read, Update, Delete
      # form에 입력한 나라
      input_country = form.data.get('country', None)
      # form에 입력한 인구 수
      input_num = form.data.get('population', None)

      CountryData.objects.update_or_create(
        #filter
        country = input_country,
        #new value
        defaults = {
          # DB에 있는 키 : form에 입력한 값
          'country': input_country,
          'population': input_num
        }
      )
      # form.save()
      # return redirect('/dashboard')
      return redirect('.')
  # form 출력
  else:
    # form 객체 생성 
    form = CountryDataForm()

  # 그래프 반영(둘 다 필요하기 때문에 안에서 처리하지 않음)


  # form 객체 생성
  form = CountryDataForm()
  # 렌더링 전달 데이터와 폼 객체 저장
  context = {'dataset':data, 'form':form}
  return render(request, 'dashboard/dashboard.html', context)


  # class CountryData(models.Model):
  # country = models.CharField(max_length=100)
  # population = models.IntegerField()
