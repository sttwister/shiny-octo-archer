# -*- coding: UTF-8 -*-
from datetime import datetime
from pytz import timezone

from django.http import HttpResponse

FORM = """
<form method='POST'>
    <input type='text' name='password'>
    <input type='submit'>
</form>
"""

WIN = """
<p>
Domnule Cătălin,
</p>

<p>
Nimeni nu credea că vei ajunge aici, dar tu ai învins imposibilul. Ești într-adevăr <strong>PROFESSIONAL</strong>!
</p>

<p>
Amu strânge pe absolut toată lumea din jur și du-te jos in beci pentru inidiciul final.
</p>
"""




bucharest = timezone('Europe/Bucharest')
deadline = datetime(2013, 6, 8, 11, 0)
deadline = bucharest.localize(deadline)

def home(request):
    amu = datetime.now(bucharest)
    remaining = amu - deadline

    msg = ''

    if request.method == 'POST':
        if request.POST['password'] == 'professional':
            if amu<deadline:
                msg = 'pretty close, try after 8pm'
            else:
                return HttpResponse(WIN)
        elif request.POST['password'] in ('ganja', 'professional', 'international'):
            msg = 'pretty close, try after 8pm'
        else:
            msg = 'marsh la kkt'

    return HttpResponse(msg + '<br />' + FORM)

