import pandas as pd

from core.models import ScheduleWorkFile


def extract_and_validate_data_from_file(file):
    if file.name.endswith('.xlsx'):
        read_file = pd.read_excel(file)
    elif file.name.endswith('.csv'):
        read_file = pd.read_csv(file, encoding='utf8')
    else:
        raise Exception(
            'Formato inválido. Verifique se o formato do arquivo é csv ou xlsx.')

    df = pd.DataFrame(read_file)

    headers = list(df)

    if not (set(ScheduleWorkFile.COLUMNS) <= set(headers)):
        raise Exception('Colunas inválidas. Verifique se o arquivo contém as seguintes colunas: {}'.format(
            ScheduleWorkFile.COLUMNS))

    return df[df.columns.unique()]
