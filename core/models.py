from django.db import models

from core.utils.date import try_parsing_date


class ScheduleWorkFile(models.Model):
    REGISTRATION = 'Matrícula'
    TECHNICIAN = 'Técnico'
    DESCRIPTION = 'Descrição da Atividade'
    DATE = 'Data'
    TIME = 'Hora'

    COLUMNS = [REGISTRATION, TECHNICIAN, DESCRIPTION, DATE, TIME]

    file = models.FileField(upload_to='imports')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """"ScheduleWorkFile Meta."""
        verbose_name = 'Importação de escalas de trabalho'
        verbose_name_plural = 'Importações de escalas de trabalho'

    def __str__(self):
        """ScheduleWorkFile string representation."""
        return str(self.file)

    def save_schedules(self, dataframe):
        schedules = []

        for item in dataframe.index:
            validated_dict = dataframe.loc[item].to_dict()

            date = '{} {}'.format(
                validated_dict[ScheduleWorkFile.DATE],
                validated_dict[ScheduleWorkFile.TIME])

            date = try_parsing_date(date)

            schedules.append(
                ScheduleWork(
                    file=self,
                    technician_name=validated_dict[ScheduleWorkFile.TECHNICIAN],
                    technician_register=str(
                        validated_dict[ScheduleWorkFile.REGISTRATION]),
                    description=validated_dict[ScheduleWorkFile.DESCRIPTION],
                    date=date)
            )

        ScheduleWork.objects.bulk_create(schedules)


class ScheduleWork(models.Model):
    file = models.ForeignKey(ScheduleWorkFile, on_delete=models.CASCADE)
    technician_name = models.CharField(max_length=127)
    technician_register = models.CharField(max_length=32)
    description = models.TextField()
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """"ScheduleWork Meta."""
        verbose_name = 'Escala de Trabalho'
        verbose_name_plural = 'Escalas de Trabalho'

    def __str__(self):
        """ScheduleWork string representation."""
        return str(self.pk)
