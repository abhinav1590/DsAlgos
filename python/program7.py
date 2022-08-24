time = input('enter a time in "HH:MM:SS am/pm" format').strip()

def converter(time):
    if time[ -2 :].lower() == 'am' and time[:2] == '12':
        return '00' + time[2:8]
    elif time[-2:].lower() == 'am':
        return time[:8]
    elif time[-2:].lower() == 'pm' and time[:2] == '12':
        return time[:8]
    else:
        return str(int(time[:2])+12) + time[2:8]

print(converter(time))

