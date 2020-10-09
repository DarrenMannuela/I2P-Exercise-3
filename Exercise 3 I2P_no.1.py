
def convert_to_days():
    hours = int(input("Enter number of hours:"))
    minutes = int(input("Enter number of minutes:"))
    seconds = int(input("Enter number of seconds:"))

    hours_to_days = hours/24
    minutes_to_days = minutes/1440
    seconds_to_days = seconds/86400

    days = round(hours_to_days + minutes_to_days + seconds_to_days, 4)

    print(days)
    return hours_to_days, minutes_to_days, seconds_to_days


convert_to_days()
