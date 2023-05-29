#%%
a = 10
b = 11
c = 0
print(a)
print(b)
c = a
a = b
b = c
print(a)
print(b)
#%%
print(a)
print(b)
a=a+b
b=a-b
a=a-b
print(a)
print(b)
# %%
print(a)
print(b)
a, b = b, a
print(a)
print(b)
# %%
import math 
x = int(input('Enter the first digit: '))
y = int(input('Enter the second digit: '))
print(f'The diference is: {int(math.fabs(x-y))} ')
# %%
x = int(input('Enter the first digit: '))
y = int(input('Enter the second digit: '))
print(f'The maximum is {max(x,y)}')
# %%
x=int(input('Type 3 digit number'))
a=x//100
b=(x//10)%10
c=(x%100)%10
x=a+10*b+100*c
print(x)