from django.shortcuts import render
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

from core.forms import ImportWorkScheduleForm
from core.models import ScheduleWork, ScheduleWorkFile
from core.utils import extract_data


@csrf_exempt
def import_work_scheduling(request):
    context = {}

    if request.method == 'POST':
        form = ImportWorkScheduleForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            data = extract_data(file)
            import_work = ScheduleWorkFile.objects.create(file=file)
            for item in data.index:
                informations = data.loc[item].to_json(force_ascii=False)
                ScheduleWork.objects.create(
                    file=import_work, informations=informations)
            messages.add_message(request, messages.SUCCESS,
                                 'Importação realizada com sucesso.')
    else:
        form = ImportWorkScheduleForm()

    context['form'] = form
    return render(request, 'core/import-work-schedule.html', context)


def schedule_list(request):
    schedules = ScheduleWorkFile.objects.all()
    return render(request, 'core/schedule.html', {'schedules': schedules})
