from django.contrib import admin

from core.models import ScheduleWork, ScheduleWorkFile


class ScheduleInline(admin.StackedInline):
    model = ScheduleWork
    extra = 1


class ScheduleWorkFileAdmin(admin.ModelAdmin):
    list_display = ('get_pk', 'get_file', 'get_created_at')
    list_display_links = ('get_pk', 'get_file')
    ordering = ['-created_at']
    search_fields = ['file']
    date_hierarchy = 'created_at'
    inlines = [ScheduleInline]

    def get_pk(self, obj):
        return obj.pk

    def get_file(self, obj):
        return obj.file

    def get_created_at(self, obj):
        return obj.created_at

    get_pk.short_description = 'ID da Importação'
    get_file.short_description = 'Arquivo'
    get_created_at.short_description = 'Data de Importação'


class ScheduleWorkAdmin(admin.ModelAdmin):
    list_display = ('get_technician_register',
                    'get_technician_name', 'get_description', 'get_date')
    list_display_links = ('get_technician_register', 'get_technician_name')
    search_fields = ['technician_register', 'technician_name']
    list_filter = ['date']

    def get_technician_register(self, obj):
        return obj.technician_register

    def get_technician_name(self, obj):
        return obj.technician_name

    def get_description(self, obj):
        return obj.description

    def get_date(self, obj):
        return obj.date

    get_technician_register.short_description = 'Matrícula'
    get_technician_name.short_description = 'Nome do Técnico'
    get_description.short_description = 'Descrição da Atividade'
    get_date.short_description = 'Data de Realização'


admin.site.register(ScheduleWorkFile, ScheduleWorkFileAdmin)
admin.site.register(ScheduleWork, ScheduleWorkAdmin)
