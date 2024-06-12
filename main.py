standard_time = input('Enter a time in standard time: ')


def convert_to_military (time):
    am_pm = input('AM or PM?')
    if time == "1200":
        if am_pm == 'AM':
            return "0000" 
        else:
            return time 
        
    if am_pm == 'PM':
        new_time = int(time) + 1200
        return str(new_time) 
    else :
        return time 
   

print(f'{standard_time} in military time is:\n {convert_to_military(standard_time)}')




