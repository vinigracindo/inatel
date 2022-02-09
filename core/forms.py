from django import forms

from core.validators import validate_file_extension


class ImportWorkScheduleForm(forms.Form):
    file = forms.FileField(
        label='Arquivo', validators=(validate_file_extension,))
