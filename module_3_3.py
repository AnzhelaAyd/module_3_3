def print_parms(a=1, b='строка', c=True):
    print(a, b, c)


print_parms()
# print_parms(a=7,b=6,c=9, d=4)   Ошибка! Не верное количество параметров
print_parms(b=25)
print_parms(c=[1, 2, 3])

values_list = [1, False, 'apple']
values_dict = {'a': 4, 'b': 6, 'c': 555}
print_parms(*values_list)
print_parms(**values_dict)

values_list_2 = ['hi', 52]
print_parms(*values_list_2, 42)
