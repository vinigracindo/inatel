from django.shortcuts import get_object_or_404, render
from django.core import serializers
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from django.contrib.auth.decorators import login_required

from core.forms import ImportWorkScheduleForm
from core.models import ScheduleWork, ScheduleWorkFile
from core.utils.get_data_file import extract_and_validate_data_from_file


@login_required
@csrf_exempt
@transaction.atomic
def import_work_scheduling(request):
    context = {}

    if request.method == 'POST':
        form = ImportWorkScheduleForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            try:
                with transaction.atomic():
                    data = extract_and_validate_data_from_file(file)
                    import_work = ScheduleWorkFile.objects.create(file=file)
                    import_work.save_schedules(data)

                    messages.add_message(request, messages.SUCCESS,
                                         'Importação realizada com sucesso.')
            except Exception as err:
                messages.add_message(request, messages.ERROR, err)
    else:
        form = ImportWorkScheduleForm()

    context['form'] = form
    return render(request, 'core/import-work-schedule.html', context)


@login_required
def schedule_list(request):
    schedules = ScheduleWorkFile.objects.all().order_by('-created_at')
    return render(request, 'core/schedule-list.html', {'schedules': schedules})


@login_required
def schedule_detail(request, schedule_pk):
    schedule = get_object_or_404(ScheduleWorkFile, pk=schedule_pk)
    schedules = serializers.serialize(
        'json',
        ScheduleWork.objects.filter(file=schedule),
        fields=('technician_name', 'technician_register', 'description', 'date')
    )

    context = {
        'schedule': schedule,
        'schedules': schedules
    }

    return render(request, 'core/schedule-detail.html', context)
