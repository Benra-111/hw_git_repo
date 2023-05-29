# %%  first task
f_n = int(input('Enter first number'))
s_n = int(input('Enter second number'))


def find_primes(f_n, s_n):
    l = []
    for i in range(f_n, s_n + 1):
        if i > 1:
            for j in range(2, i):
                if (i % j) == 0:
                    break
            else:
                l.append(i)
    return l


find_primes(f_n, s_n)
print(find_primes(f_n, s_n))


# %%  second task
s = str(input(''))


def unique_characters1(s: str) -> bool:
    return (len(set(s)) == len(s))


unique_characters1(s)
# %%  second task other answer
s = str(input(''))


def unique_characters2(s: str) -> bool:
    for i in s:
        if s.count(i) > 1:
            return False
    return True


unique_characters2(s)
# %% second task other answer
s = 'asdf'


def unique_characters3(s):
    for i in range(len(s)):
        if (s[i] in s[i+1:len(s)]):
            return False
    return True


unique_characters3(s)
# %% third task


def fibonacci_nums(number_of_itterations: int) -> list:
    fibonacci_list = [1, 1]
    for i in range(number_of_itterations - 2):
        a = fibonacci_list[i] + fibonacci_list[i + 1]
        fibonacci_list.append(a)
    return fibonacci_list[number_of_itterations-1], fibonacci_list


number_of_itterations = int(input('Number of itterations'))
fibonacci_nums(number_of_itterations)
# %%


def swapcase(string_input: str) -> str:
    list_of_chars = list(string_input)
    for i in range(0, len(list_of_chars)):
        if list_of_chars[i].isupper():
            list_of_chars[i] = list_of_chars[i].lower()
        else:
            list_of_chars[i] = list_of_chars[i].upper()
    print(''.join(list_of_chars))


st = str(input(''))

swapcase(st)
# %%


def swapcase() -> str:
    list_of_chars = list(string_input)
    for i in range(0, len(list_of_chars)):
        if list_of_chars[i].isupper():
            list_of_chars[i] = list_of_chars[i].lower()
        else:
            list_of_chars[i] = list_of_chars[i].upper()
    print(''.join(list_of_chars))


string_input = str(input(''))

swapcase()

# %%


def simple_interest() -> float:
    initial = int(input(''))
    interest = float(input(''))
    years = int(input())
    for i in range(years):
        initial = initial * (1 + interest)
    return round(initial, 2)


simple_interest()
# %%


def pasword_strength() -> int:
    s = set(input(''))
    rate = len(s)
    for i in s:
        if i.isupper():
            rate = rate + 2
        elif i.islower():
            rate = rate + 3
        elif i.isdigit():
            rate = rate + 4
        elif (i.isupper()) == False and (i.isdigit() == False):
            rate = rate + 5
    return rate


pasword_strength()
# %%


def pasword_strength() -> int:
    s = str(input(''))
    rate = len(s)
    for i in s:
        if s.count(i) > 1:
            continue
        elif i.isupper():
            rate = rate + 2
        elif i.islower():
            rate = rate + 3
        elif i.isdigit():
            rate = rate + 4
        elif (i.isupper()) == False and (i.isdigit() == False):
            rate = rate + 5
    return rate


pasword_strength()
# %%
