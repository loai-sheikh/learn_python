str_with_format = "this {0} is a {1}".format('python','placeholder')
print(str_with_format)
str_with_format_arg = "this {arg} is a {x}".format(arg='python',x='placeholder')
print(str_with_format_arg)


str_ff = 'this is %s formatted %s' %('a','strings')
print(str_ff)

str_a = 'bill'
str_with_a = f"this is a {str_a}"
print(str_with_a)

from string import Template
string_template = Template("$who was the $what")
print(string_template.substitute(who="Jon",what ="winner"))