standard_time = input('Enter a time in standard time: ')
am_pm = input('AM or PM?')


def convert_to_military (time, time_of_day) :
    if time == "1200":
        if time_of_day == 'AM':
            return "0000"
        else:
            return time
        
    if time_of_day == 'PM':
        new_time = int(time) + 1200
        return str(new_time)
    else :
        return time
   
# print(standard_time + ' in military time is:\n' + convert_to_military(standard_time, am_pm))
print(f'{standard_time} in military time is:\n {convert_to_military(standard_time, am_pm)}')