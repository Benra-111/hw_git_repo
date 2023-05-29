#%%
print ( False == (not True) )
print ( True and False == (True and False) )
print ( not (True and "A" == "B") )
# %%
weight = 0.065 #weight of one grain in grams
amount_of_grains = 1
cell_num = 1
while cell_num < 64:
    amount_of_grains = 2 ** cell_num + amount_of_grains
    cell_num += 1
all_weight_in_tonns = (amount_of_grains * weight) / 1000000
answer_str = str(all_weight_in_tonns)
print(f'Weight in tonns: {answer_str}')
# %%
number = int(input('Your number'))
counter = 1 
list_factors = []
while counter <= number:
    if number % counter == 0:
        list_factors.append(counter)
    counter = counter + 1
print(f'The factors of {number} are:', end = ' ')
print(*list_factors, sep = ', ')
# %%
side_a = int(input('Enter the side a of triangle: '))
side_b = int(input('Enter the side b of triangle: '))
side_c = int(input('Enter the side c of triangle: '))
if side_a == side_b and side_a == side_c:
    print('The triangle is equilateral and isosceles')
elif side_a == side_b or side_a == side_c or side_b == side_c:
    print('The triangle is isosceles')
else:
    print('The triangle is scalene')
# %% Answer if there always 31 day in month
year = int(input('Enter the year: '))
month = int(input('Enter the number of month: '))
day = int(input('Enter the day: '))
if day == 31:
    day = 1
    month += 1
if month >= 12:
    month = 1
    year += 1
print(f'The next date is: {year}-{month}-{day}')
# %% Answer in real months
year = int(input('Enter the year: '))
month = int(input('Enter the number of month: '))
day = int(input('Enter the day: '))
list_month_31 = [1, 3, 5, 7, 8, 10, 12]
list_month_30 = [4, 6, 9, 11]
real_date = True
if month in list_month_31 and day == 31:
    day = 1
    month += 1
    if day > 31:
        print('Incorrect input')
        real_date = False
elif month in list_month_30 and day == 30:
    day = 1
    month += 1
    if day > 30:
        print('Incorrect input')
        real_date = False
elif month == 2:
    if year % 4 == 0 and day == 29:
        day = 1
        month += 1
    elif year % 4 != 0 and day == 28:
        day = 1
        month += 1
    else:
        if day > 29:
            print('Incorrect input')
            real_date = False
        day = day + 1   
else:
    day = day + 1
if month == 13 and real_date == True:
    month = month - 12 
    year += 1
if real_date == True:
    print(f'The next date is: {year}-{month}-{day}')
else:
    print(f'{real_date} Date')
# %%
