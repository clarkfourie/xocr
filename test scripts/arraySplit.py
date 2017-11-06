# turn string to char array to select individual words

given_names = ''
tmp_given_names = "GEORGE ARCHIBALD CLARK"

name_array = tmp_given_names.split(" ")
i = 1
for i in range(len(name_array)):
	given_names += name_array[i] + ' '

first_name = tmp_given_names.split(" ")[0]

print(given_names)
print(first_name)