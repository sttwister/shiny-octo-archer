from datetime import datetime
from pytz import timezone

from django.http import HttpResponse

def home(request):
    bucharest = timezone('Europe/Bucharest')
    return HttpResponse('%s' % datetime.now(bucharest))
