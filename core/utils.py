from django.forms import ValidationError
import pandas as pd


def extract_data(file):
    if file.name.endswith('.xlsx'):
        read_file = pd.read_excel(file)
    elif file.name.endswith('.csv'):
        read_file = pd.read_csv(file, encoding='utf8')
    else:
        return None

    df = pd.DataFrame(read_file)

    return df
