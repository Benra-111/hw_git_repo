# %%
def change_hat_state(a, list_, i):
    a = (a * i) - 1
    if list_[a] == 1:
        list_[a] = 0
    elif list_[a] == 0:
        list_[a] = 1
    return list_


def cat_manipulation(n, list_, i):
    for j in range((n // i) + 1):
        change_hat_state(j, list_, i)
    return list_


def lll():
    n = int(input('Number of cats: ')) + 1
    list_ = [0] * n
    for i in range(1, n + 1):
        cat_manipulation(n, list_, i)
    list__ = [list_[n-1]] + list_[1:n-1]

    return list__


print(lll())

# %%
