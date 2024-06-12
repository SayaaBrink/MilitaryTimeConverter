

def convert_to_military (time):
    am_pm = input('AM or PM?')
    if time == 1200:
        if am_pm == 'AM':
            return 0000 
        else:
            return time 
        
    if am_pm == 'PM':
        new_time = time + 1200
        return str(new_time) 
    else :
        return time 
    


def convert_to_standard(time):
    if time <= 1200:
        return str(time) + ' AM'
    else:
        new_time = time - 1200
        return str(new_time) + ' PM'



def choose_conversion ():
    conversion_choice = input('Convert to: ')

    if conversion_choice != 'standard' and conversion_choice != 'military':
        print('Invalid response')
        choose_conversion()

    time = int(input('Enter a time: '))
   
    if conversion_choice == 'military':
        time_in_military = convert_to_military(time)
        print(f'{time} in military time is:\n {time_in_military}')

    else:
        time_in_standard = convert_to_standard(time)
        print(f'{time} in standard time is:\n {time_in_standard}')


choose_conversion()