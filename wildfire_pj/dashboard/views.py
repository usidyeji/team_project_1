from django.shortcuts import render
from .models import WildFire_day, WildFire_time, MonthCause
from django.db import connection
# from .forms import Wildfire_timeDataForm
# Create your views here.
# def dashboard(request, dmgarea, tempavg):
#     ydata = Wildfire.objects.all(dmgarea=dmgarea)
#     xdata = Wildfire.objects.all(tempavg=tempavg)

#     form = WildfireDataForm()

#     context =
def dashboard(request):
  # 요인별
  cursor = connection.cursor()

  cause = "SELECT cause, SUM(count) FROM dashboard_monthcause GROUP BY cause"
  result = cursor.execute(cause)
  datac = cursor.fetchall()

  connection.commit()
  connection.close()
  cause = []
  for c_data in datac:
    row = {'cause':c_data[0], 'csum':c_data[1]}
    cause.append(row)
    
  # 월 별
  cursor = connection.cursor()

  month = "SELECT `month`, SUM(count) FROM dashboard_monthcause GROUP BY `month`"
  result = cursor.execute(month)
  datam = cursor.fetchall()

  connection.commit()
  connection.close()
  month = []
  for m_data in datam:
    row = {'month':m_data[0], 'msum':m_data[1]}
    month.append(row)


  # 요일별
  cursor = connection.cursor()
  strSql = "SELECT day, SUM(count) FROM dashboard_wildfire_day GROUP BY day"
  result = cursor.execute(strSql)
  d_datas = cursor.fetchall()
  connection.commit()
  connection.close()
  day = []
  for d_data in d_datas:
      row = {'day':d_data[0], 'dsum':d_data[1]}
      day.append(row)

  # 시간별
  cursor = connection.cursor()
  # 시간별 산불발생횟수, MySQL 쿼리문으로 데이터 불러오기
  strSql = "SELECT time, SUM(count) FROM dashboard_wildfire_time GROUP BY time"
  result = cursor.execute(strSql)
  datat = cursor.fetchall()

  connection.commit()
  connection.close()
  time = []
  for t_data in datat:
      row = {'time':t_data[0], 'tsum':t_data[1]}
      time.append(row)

  context = {'time_data':time, 'cause_data':cause,
'month_data':month, 'day_data':day }

  return render(request, 'dashboard/dashboard.html',context)