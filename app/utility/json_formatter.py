import datetime


def defaultFormatter(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()
    else:
        return str(o)