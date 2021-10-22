import datetime


MONTH_TO_NUMERIC = {
    "Jan": " 01",
    "Feb": " 02",
    "Mar": " 03",
    "Apr": " 04",
    "May": " 05",
    "Jun": " 06",
    "Jul": " 07",
    "Aug": " 08",
    "Sep": " 09",
    "Oct": " 10",
    "Nov": " 11",
    "Dec": " 12",
}


def month_to_numeric(datetime_string):
    datetime_list = datetime_string.split(" ")
    for index, item in enumerate(datetime_list):
        if item in MONTH_TO_NUMERIC:
            datetime_list[index] = MONTH_TO_NUMERIC[item]
    return ' '.join(datetime_list)


def to_datetime(datetime_string):
    offset_sign = datetime_string[-5]
    offset_hours = int(datetime_string[-4:-2] if datetime_string[-4] != "0" else datetime_string[-3])
    offset_minutes = int(datetime_string[-2:] if datetime_string[-2] != "0" else "0")
    offset = datetime.timedelta(hours=offset_hours, minutes=offset_minutes)

    if offset_sign == "-":
        offset = datetime.timedelta(0) - offset

    datetime_string = month_to_numeric(datetime_string)

    datetime_object = datetime.datetime.strptime(datetime_string[4:-6], "%d %m %Y %H:%M:%S")
    return datetime_object - offset


def time_delta(t1, t2):
    return str(int(abs((to_datetime(t2) - to_datetime(t1)).total_seconds())))


t1 = "Sun 10  05 2015 13:54:36 -0700"
t2 = "Sun 10 May 2015 13:54:36 -0000"
t3 = "Sat 02 May 2015 19:54:36 +0530"
t4 = "Fri 01 May 2015 13:54:36 -0000"

print(to_datetime(t1))
print(to_datetime(t2))
print(to_datetime(t3))
print(to_datetime(t4))
print(time_delta(t1, t2))
print(time_delta(t3, t4))
