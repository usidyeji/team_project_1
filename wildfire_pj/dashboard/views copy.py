from itertools import count
from django.shortcuts import render
from .models import Wildfire, MonthCause, WildFire_day, WildFire_time
from django.db import connection

def dashboard(request):
  
  cursor = connection.cursor()

  strSql = "SELECT time, SUM(count) FROM dashboard_wildfire_time GROUP BY time"
  result = cursor.execute(strSql)
  datas = cursor.fetchall()

  connection.commit()
  connection.close()
  time = []
  for t_data in datas:
      row = {'time':t_data[0], 'sum':t_data[1]}
      time.append(row)
  context = {'time_data':time}

  return render(request, 'dashboard/dashboard.html', context)


# Create your views here.

# def dashboard(request):
#   data = Wildfire.objects.all()

# # cause
#   cm = MonthCause.objects.filter(cause='입산자실화').values('count')
#   cm = sum(list(m['count'] for m in cm))
#   cf = MonthCause.objects.filter(cause='논밭두렁소각').values('count')
#   cf = sum(list(m['count'] for m in cf))
#   ct = MonthCause.objects.filter(cause='쓰레기소각').values('count')
#   ct = sum(list(m['count'] for m in ct))
#   cs = MonthCause.objects.filter(cause='담뱃불실화').values('count')
#   cs = sum(list(m['count'] for m in cm))
#   csu = MonthCause.objects.filter(cause='성묘객실화').values('count')
#   csu = sum(list(m['count'] for m in cm))
#   cp = MonthCause.objects.filter(cause='불장난').values('count')
#   cp = sum(list(m['count'] for m in cm))
#   cb = MonthCause.objects.filter(cause='건축물화재').values('count')
#   cb = sum(list(m['count'] for m in cm))
#   ce = MonthCause.objects.filter(cause='기타').values('count')
#   ce = sum(list(m['count'] for m in cm))

#   cause = [cm, cf, ct, cs, csu, cp, cb, ce]


#   # month
#   jan = MonthCause.objects.filter(month='1월').values('count')
#   jan = sum(list(m['count'] for m in jan))
#   feb = MonthCause.objects.filter(month='2월').values('count')
#   feb = sum(list(m['count'] for m in feb))
#   mar = MonthCause.objects.filter(month='3월').values('count')
#   mar = sum(list(m['count'] for m in mar))
#   apr = MonthCause.objects.filter(month='4월').values('count')
#   apr = sum(list(m['count'] for m in apr))
#   may = MonthCause.objects.filter(month='5월').values('count')
#   may = sum(list(m['count'] for m in may))
#   june = MonthCause.objects.filter(month='6월').values('count')
#   june = sum(list(m['count'] for m in june))
#   july = MonthCause.objects.filter(month='7월').values('count')
#   july = sum(list(m['count'] for m in july))
#   aug = MonthCause.objects.filter(month='8월').values('count')
#   aug = sum(list(m['count'] for m in aug))
#   sep = MonthCause.objects.filter(month='9월').values('count')
#   sep = sum(list(m['count'] for m in sep))
#   oct = MonthCause.objects.filter(month='10월').values('count')
#   oct = sum(list(m['count'] for m in oct))
#   nov = MonthCause.objects.filter(month='11월').values('count')
#   nov = sum(list(m['count'] for m in nov))
#   dec = MonthCause.objects.filter(month='12월').values('count')
#   dec = sum(list(m['count'] for m in dec))


#   # days
#   mon = WildFire_day.objects.filter(day='Mon').values('count')
#   mon = sum(list(m['count'] for m in mon))
#   tue = WildFire_day.objects.filter(day='Tues').values('count')
#   tue = sum(list(m['count'] for m in tue))
#   wed = WildFire_day.objects.filter(day='Wed').values('count')
#   wed = sum(list(m['count'] for m in wed))
#   thu = WildFire_day.objects.filter(day='Thur').values('count')
#   thu = sum(list(m['count'] for m in thu))
#   fri = WildFire_day.objects.filter(day='Fri').values('count')
#   fri = sum(list(m['count'] for m in fri))
#   sat = WildFire_day.objects.filter(day='Sat').values('count')
#   sat = sum(list(m['count'] for m in sat))
#   sun = WildFire_day.objects.filter(day='Sun').values('count')
#   sun = sum(list(m['count'] for m in sun))
#   holi = WildFire_day.objects.filter(day='Holi').values('count')
#   holi = sum(list(m['count'] for m in holi))

#   days = [mon, tue, wed, thu, fri, sat, sun, holi]
#   # times
#   am = WildFire_time.objects.filter(time='오전(6~10시)').values('count')
#   am = sum(list(m['count'] for m in am))



#   context = {'dataset':data, 'cause':cause,
#   'jan':jan, 'feb':feb, 'mar':mar, 'apr':apr, 'may':may, 'june':june, 'july':july, 'aug':aug, 'sep':sep, 'oct':oct, 'nov':nov, 'dec':dec,
#   'days':days
#   # context = {'dataset':data, 'dos':do_cnt}

#   return render(request, 'dashboard/dashboard.html', context)

   # class CountryData(models.Model):
  # country = models.CharField(max_length=100)
  # population = models.IntegerField()
