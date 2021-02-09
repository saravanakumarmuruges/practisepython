def timeConversion(s):
    if(s[-2:] == 'AM' and s[0:2] == '12'):
        return f'00:{s[3:5]}:{s[6:8]}'
    elif(s[-2:] == 'AM' and s[0:2] != '12'):
        return s[0:8]
    elif(s[-2:] == 'PM' and s[0:2] == '12'):
        return s[0:8]
    elif(s[-2:] == 'PM' and s[0:2] != '12'):
        return f'{int(s[0:2])+12}:{s[3:5]}:{s[6:8]}'
    else:
        return 'Enter valid time stamp'

print(timeConversion('12:45:54PM'))


