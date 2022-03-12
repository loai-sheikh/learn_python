my_str = 'abcdefg'
#print string 3 times
print(my_str*3)
print('***************************')
#print first charachter
print(my_str[0])
#print 2-5 charachter
print(my_str[2:5])
#print first 5 charachter
print(my_str[:5])
#print from first 2 charachter until the end
print(my_str[2:])
#print and skip 1 characters steps
print(my_str[::2])
#print reverse string
print(my_str[::-1])
print('***************************')
#print string with tabs
print('hello\tworld')
print('***************************')
mystring = 'hellopython'
print(mystring.capitalize())
print(mystring.center(100,' '))
print(mystring.count('l'))
print(mystring.startswith('h'))
print(mystring.endswith('n'))
print(mystring.find('n'))
print(mystring.isalpha())
my_number = '123'
print(my_number.isdigit())

my_space = '   '
print(my_space.isspace())
print(len(my_number))
mix_string = 'ABcDe'
print(mix_string.upper())
print(mystring.lower())
spacing_string = '  hello '
print(spacing_string.strip())
print('***************************')
#split str
split_str = str.split('hello my name is pythom')
print(split_str)
join_str = ' '.join(split_str)
print(join_str)