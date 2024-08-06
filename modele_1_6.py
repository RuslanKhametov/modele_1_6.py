my_dict = {'Ruslan' : 1995, 'Ayrat' : 1969, 'Emilya' : 2003}
print(my_dict)
print(my_dict['Ruslan'])
print(my_dict.get ('Semen' , 'Отсутствует'))
my_dict.update({'Lylia' : 1963,
                'Samira' : 2007})
print(my_dict)
del my_dict['Ayrat']
print(my_dict)

my_set = {1, 13, 1, 5, 13, 7, 'sistym', (1, 2, 1)}
print(my_set)
my_set.add(123)
my_set.add(2)
my_set.remove('sistym')
print(my_set)

