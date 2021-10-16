# Problems

1. [Unique Email Addresses](unique_email_addresses)
2. [Add Two Numbers](add_two_numbers)
3. [Two Sum](two_sum)
4. [All You Can Eat](all_you_can_eat)
5. [Tennis Game](tennis_game)
6. [Validate Binary Search Tree](validate_binary_search_tree)
7. [Magic Stones](magic_stones)

# Tips

Some useful tips to play games.

### Get string of ASCII letters
```Python
letters = ''.join([chr(i) for i in range(97, 123)])  # lower characters
letters += ''.join([chr(i) for i in range(65, 91)])  # upper characters
```

### Get string of numbers
```Python
numbers = ''.join([str(i) for i in range(0, 10)])
```

### Convert a string to a list of characters
```Python
characters = list(string)
```

### Get ASCII code of a character
```Python
ascii_code = ord(c)  # c is a character
```

### Get character from an ASCII code
```Python
c = chr(ascii_code)  # ascii_code is an integer
```

### Padding a string
```Python
txt = '*'
print(txt.rjust(5))
# return
# '    *' (4 spaces before the star)

print(txt.ljust(5))
# return
# '*    ' (4 spaces after the star)
