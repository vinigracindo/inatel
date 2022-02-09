def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.csv', '.xlsx']
    if not ext.lower() in valid_extensions:
        raise ValidationError(
            'Extensão não suportada. Anexe um arquivo CSV ou XLSX.')
