#each element in list
num = [1, 2, 4]
more_num = [*num, 21, 31]

print(*more_num, sep='-')


#each element in each list
def transpose_list(list_of_lists):
	return [
		list(row) for row in zip(*list_of_lists)
	]

print(transpose_list(([1, 2], [3, 4], [5, 6])))


#use format with key-value pair/dictionary
date_info = {'y':'2020', 'm':'01', 'd':'21'}
filename = '{y}-{m}-{d}.txt'.format(**date_info)

print(filename)

#unpack list
fruits = ['lemon', 'pear', 'watermelon', 'tomato']
first, second, *remaining = fruits

print(*remaining, first, second)

first, *middle, last = fruits

print(*middle)

#another unpack fruits
print(fruits[1:], fruits[0])


#merge dictionary
date_info = {'y':'2020', 'm':'01', 'd':'21'}
track_info = {'artist': 'Beethoven', 'title': 'Symphony No. 5'}

all_info = {**date_info, **track_info, 'group': 'Meetup'}

print(all_info)

#another merge dictionary duplicate with update

new_info = {**date_info, **track_info, 'y': '2021'}

print(new_info)