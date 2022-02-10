from datetime import datetime


def try_parsing_date(text):
    text = text.split(' ')
    text = '{} {}'.format(text[0], text[-1])
    for fmt in ('%d/%m/%Y %H:%M:%S', '%Y-%m-%d %H:%M:%S'):
        try:
            return datetime.strptime(text, fmt)
        except ValueError:
            pass
    raise ValueError('no valid date format found')
