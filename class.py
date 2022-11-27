a = [1, 5, 9, 78, 96, 1, 6, 9]
b = set(a)
if len(a)==len(b):
    print('дубликатов нет')
else:
    print('дубликаты есть')

dict = {1:1, 2:4, 3:9, 4:16, 5:25}
print(dict)
dict['7'] = 49
print(dict)
dict[(8,)] = [6, 4]
print(dict)
print(dict[3])
del dict[2]
print(dict)
print(dict.keys())


set = {1, 5, 8, 9, 'a', 'b', 6, 'g', 2.3, 6.5}
set1 = frozenset([1, 7, 89, 'a', 2, 'k'])
print(set|set1)
print(set&set1)

