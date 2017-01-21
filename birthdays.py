birthdays = {'Hannah': 'April 22',
             'Aimée': 'May 11',
             'Tracy': 'April 7',
             'Craig': 'November 6'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('When is their birthday?')
        bday = input()
        if bday == '':
            break
        else:
            birthdays[name] = bday
            print('B')