# %%
from collections import Counter
_str = 'hjfnjhhfkiy;oiufddfhkh'
_list = list(_str)
print(_list)
_list.sort()
for i in range(len(_list)):
    _str_1 = _str.append(_list[i])
print(_str_1)
# %%


def check(x):
    for a in range(1, x):
        if x % a != 0:
            break
    return False


_list = [x for x in range(3, 100) if check(x)]
print(_list)

# %%
_tuple = (1, 2, 3)
_tuple_1 = str(_tuple[:])
_tuple_1 = _tuple_1.replace(', ', '')
print(_tuple, '-', type(_tuple), '   ->   ', _tuple_1, '-', type(_tuple_1))
for i in _tuple_1:
    print(i)

# %%
_s = '12,3'
_i = int(_s)
print(f'{_i}, {type(_i)}')
# %%
_s = '12, 3'
_s = _s.split(', ')
_l = [i for i in _s if i.isdigit()]
print(f'{(_l)}, {type(_l)}')
# %%


def compute_difference(first: list, second: list) -> tuple:
    first_minus_second = [item for item in first if item not in second]
    second_minus_first = [item for item in second if item not in first]
    return (first_minus_second, second_minus_first)


def test_compute_difference():
    result1 = compute_difference(['a', 'b', 'c', 'c', 'd'], ['c', 'd', 'e'])
    assert result1 == (['a', 'b', 'c'], ['e'])
    result2 = compute_difference([], ['c', 'd', 'e'])
    assert result2 == ([], ['c', 'd', 'e'])
    result3 = compute_difference([1, 2, 3], [4, 4, 5, 6])
    assert result3 == ([1, 2, 3], [4, 4, 5, 6])
    result3 = compute_difference([1, 2, 3], [2, 3, 4])
    assert result3 == ([1], [4])


test_compute_difference()
compute_difference(['a', 'b', 'c', 'c', 'd'], ['c', 'd', 'e'])
# %%


def compute_difference(first: list, second: list) -> tuple:
    first_counter = Counter(first)
    second_counter = Counter(second)

    first_minus_second = []
    second_minus_first = []

    for item, count in first_counter.items():
        if count > second_counter.get(item, 0):
            first_minus_second.extend([item] * (count - second_counter[item]))

    for item, count in second_counter.items():
        if count > first_counter.get(item, 0):
            second_minus_first.extend([item] * (count - first_counter[item]))

    return (first_minus_second, second_minus_first)


def test_compute_difference():
    result1 = compute_difference(['a', 'b', 'c', 'c', 'd'], ['c', 'd', 'e'])
    assert result1 == (['a', 'b', 'c'], ['e'])
    result2 = compute_difference([], ['c', 'd', 'e'])
    assert result2 == ([], ['c', 'd', 'e'])
    result3 = compute_difference([1, 2, 3], [4, 4, 5, 6])
    assert result3 == ([1, 2, 3], [4, 4, 5, 6])
    result3 = compute_difference([1, 2, 3], [2, 3, 4])
    assert result3 == ([1], [4])


test_compute_difference()
compute_difference(['a', 'b', 'c', 'c', 'd'], ['c', 'd', 'e'])
# %%
