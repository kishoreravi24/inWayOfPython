a = 'spam msg'
print(a)

b = 'spam msg with escaping single quotes \'hello\''
print(b)

c = '"yes", they said about the spam msgs'
print(c)

#\n problems
# d='c:\some\name' -> \n excludes the ' , for that we need to have r i.e raw string
d = r'c:\some\name'
print(d)

# string literals
print("""\
        Usage: [OPTIONS]
        -h       Display the help message
        --help   Display the help message
""")

e = 3*'un'+'ium'
print(e)

# some string indexes
word = "hello world"
print(word[-1],word[-2],word[0:2])
print(len(word))

# string methods i.e string libraries
str_word = "hello world string test"
print(str_word.upper())
print(str_word.lower())

str_word_space = "     hello, world!     "
print(str_word_space.strip())

str_word_split = "hello,world"
print(str_word_split.split())

str_word_join = ['hello','world']
joined_string = '-'.join(str_word_join)
print(joined_string)

str_word_find = "hello, world!"
print(str_word_find.find("world"))

str_word_replace = "hello, world!"
print(str_word_replace.replace("hello","hi"))

str_word_format_1 = "hello"
str_word_format_2 = "world"
print("{} {} I am kishore".format(str_word_format_1,str_word_format_2))

