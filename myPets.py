myPets = ['Sophie', 'Pooka', 'Fat-Tail']
print('Enter a pet name')
name = input()
if name not in myPets:
    print('I don''t have a pet called' + name)
else:
    print(' Yes, I do have a pet called ' + name)

