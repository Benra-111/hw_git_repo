#%% 1 
print(3 < 4)
print(10 >= 5)
print(42 != '42')
# %% 1
print("""The quote: "The quote" """)
# %% 2
new_input = str(input('Your palindrome here: '))
#print(new_input)
length = (len(new_input))#length of palindrome
#print(length)
l= length // 2
#print(l)
l1= -1 * l
#print(l1)
#print(new_input[-1:l1-1:-1])
#print(new_input[0:l:])
if new_input[0:l:] == new_input[-1:l1-1:-1] or new_input == 'palindrome':
    print('It is palindrome')
else:
    print('It\'s not palindrome')
# %% 3
uname = str(input('Your name '))
uage = str(input('Your age '))

print("Your name is", uname + ", and you\'re", uage + " years old.")

print(f'Your name is {uname}, and you\'re {uage} years old.')

sentance = 'Your name is {name}, and you\'re {age} years old.'
print(sentance.format(age=uage, name=uname))
# %% 4
string_1 = 'Animals'
string_2 = ' Badger'
string_3 = '  HonyPot  '
string_1 = string_1.lower()
string_2 = string_2.upper()
string_3_ = string_3.strip()
string_3_r = string_3.rstrip()
string_3_l = string_3.lstrip()
print(string_1)
print(string_2)
print('|' + string_3_ + '|')
print('|' + string_3_r + '|')
print('|' + string_3_l + '|')

# %% 6
bear_1 = 'Bear'
bear_2 = 'bear'
bear_3 = 'BEAR'
bear_4 = 'bEAr'
print(bear_1[:2:] == 'Be')
print('Be' in bear_2)
print('Be' in bear_3)
print(bear_4[:2:] == 'Be')
bear_21 = bear_2.capitalize()
bear_31 = bear_3.capitalize()
bear_41 = bear_4.capitalize()
print('after the trasition')
print('Be' in bear_21)
print('Be' in bear_31)
print('Be' in bear_41)
# %% 7
coded_text = 'X!xeXnxiXlX XtxeXrxcXeXsX Xax XsX`XtXIX'
coded_text = coded_text[::-1]
coded_text = coded_text.replace('X', '')
coded_text = coded_text.replace('x', '')
print(coded_text)
# %%
