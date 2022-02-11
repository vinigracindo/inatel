from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from logs.models import Log


@login_required
def list_logs(request):
    logs = Log.objects.all().using('logs').order_by('-date')
    return render(request, 'logs/list.html', {'logs': logs})


@login_required
def view_reqres(request, log_pk):
    log = get_object_or_404(Log, pk=log_pk)
    return render(request, 'logs/view.html', {'log': log})
