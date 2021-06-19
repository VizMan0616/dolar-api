from flask_restful import fields
from datetime import datetime

RESOURCE_FIELDS = {
    'dollar_quantity': fields.Float,
    'bolivar_quantity': fields.Float,
    'date_asked': fields.DateTime
}


def DOLLAR_URL():
    now = datetime.now()

    if now.strftime('%A') == 'Saturday':
        return f'https://monitordolarvzla.com/promedio-del-dolar-{str((now.day-1)).zfill(2)}-{str(now.month).zfill(2)}-{now.year}-1-pm/'
    if now.strftime('%A') == 'Sunday':
        return f'https://monitordolarvzla.com/promedio-del-dolar-{str((now.day-1)).zfill(2)}-{str(now.month).zfill(2)}-{now.year}-1-pm/'

    if now.hour > 9 and now.hour < 13:
        return f'https://monitordolarvzla.com/promedio-del-dolar-{str(now.day).zfill(2)}-{str(now.month).zfill(2)}-{now.year}-9-am/'
    if now.hour < 9:
        return f'https://monitordolarvzla.com/promedio-del-dolar-{str((now.day-1)).zfill(2)}-{str(now.month).zfill(2)}-{now.year}-1-pm/'

    return f'https://monitordolarvzla.com/promedio-del-dolar-{str(now.day).zfill(2)}-{str(now.month).zfill(2)}-{now.year}-1-pm/'
