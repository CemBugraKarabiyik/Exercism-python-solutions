def add(moment):
    import datetime
    new = moment + datetime.timedelta(seconds=1000000000)
    return new
