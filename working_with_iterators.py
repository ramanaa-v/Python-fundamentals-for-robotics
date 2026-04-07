my_list = [1, 2, 3, 4, 5]
my_iterator = iter(my_list)

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print('')

my_iterator = iter(my_list)
for item in my_iterator:
    print(item)