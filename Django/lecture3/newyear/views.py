from django.shortcuts import render
from datetime import datetime as dt

# Create your views here.
def index(request):
    # date = dt(2022, 1, 1)
    date = dt.now()
    # if date.month == 1 and date.day == 1:
    #     answer = "YES"
    # else:
    #     answer = "NO"
    context = {'answer': date.month == 1 and date.day == 1}
    return render(request, 'newyear/index.html', context=context)
