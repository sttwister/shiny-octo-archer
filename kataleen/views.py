from datetime import datetime
from pytz import timezone

from django.http import HttpResponse

bucharest = timezone('Europe/Bucharest')
deadline = datetime(2013, 6, 8, 11, 0)
deadline = bucharest.localize(deadline)

def home(request):
    amu = datetime.now(bucharest)
    remaining = amu - deadline
    if amu<deadline:
        return HttpResponse('too soon')
    else:
        return HttpResponse('is ok')

