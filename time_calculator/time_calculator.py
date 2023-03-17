def add_time(start, duration, day=False):
    a = start.split(" ")
    b = a[0].split(":")
    add = duration.split(":")
    hoursadd = int(add[0])
    minutesadd = int(add[1])
    hours=int(b[0])
    minutes=int(b[1])
    days = 0
    if a[1] == "PM":
        hours+=12
    new_time = 0
    minutes += minutesadd
    hours += hoursadd
    while minutes > 59:
        minutes+=-60
        hours+=1
    while hours > 24:
        hours+=-24
        days+=1
    tod = ""
    if hours == 24:
        hours+=-12
        tod = "AM"
        days+=1
    elif hours == 12:
        tod = "PM"
    elif hours> 12:
        hours+=-12
        tod = "PM"
    else:
        tod = "AM"
    if minutes<10:
        minutes = "0"+str(minutes)


    time = str(hours)+":"+str(minutes)+" "+tod

    if day == False:
        if days == 1:
            return time + " (next day)"
        elif days == 0:
            return time
        else:
            return time + " ("+str(days)+" days later)"

    week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    day = day.lower()
    day = day.capitalize()
    day = week.index(day)
    if isinstance(day,int):
        day += days
        day = day%7
        day = week[day]

    if days == 1:
        return time +", "+day+" (next day)"
    elif days == 0:
        return time+", "+day
    else:
        return time +", "+day+" ("+str(days)+" days later)"
    return new_time
