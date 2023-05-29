# %%
# first-second: ['a', 'b']
# second-first: ['e']


def compute_difference(first: list, second: list) -> tuple:
    _list_1 = []
    _list_2 = []
    combined_lists = first[:]
    combined_lists.extend(second)
    for symbol in combined_lists:
        a = first.count(symbol)
        b = second.count(symbol)
        c = a - b
        if c > 0 and (symbol in _list_1) == False:
            _list_1.extend([symbol for i in range(c)])
        elif c < 0 and (symbol in _list_2) == False:
            _list_2.extend([symbol for i in range(abs(c))])
    returning_value = (_list_1, _list_2)
    return returning_value


def test_compute_difference():
    result1 = compute_difference(['a', 'b', 'c', 'c',  'd'], ['c', 'd', 'e'])
    assert result1 == (['a', 'b', 'c'], ['e'])
    result2 = compute_difference([], ['c', 'd', 'e'])
    assert result2 == ([], ['c', 'd', 'e'])
    result3 = compute_difference([1, 2, 3], [4, 4, 5, 6])
    assert result3 == ([1, 2, 3], [4, 4, 5, 6])
    result3 = compute_difference([1, 2, 3], [2, 3, 4])
    assert result3 == ([1], [4])


test_compute_difference()

# %%


def sum_of_two(nums: list, target: int) -> list:
    # write your code here
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def test_sum_of_two():
    result1 = sum_of_two([2, 7, 11, 15], 9)
    assert result1 == [0, 1]
    result2 = sum_of_two([3, 2, 4], 6)
    assert result2 == [1, 2]
    result3 = sum_of_two([3, 3], 6)
    assert result3 == [0, 1]


test_sum_of_two()

# %%


def unique_elements(arr: list) -> list:
    # write your code here
    unique_list_ = []
    for symbol in arr:
        a = arr.count(symbol)
        if a == 1:
            unique_list_.append(symbol)
    return unique_list_


def test_unique_elements():
    result1 = unique_elements([1, 2, 3, 2, 4, 5, 5])
    assert result1 == [1, 3, 4]
    result2 = unique_elements([1, 2, 3, 4, 5])
    assert result2 == [1, 2, 3, 4, 5]
    result3 = unique_elements([1, 1, 1, 1, 1])
    assert result3 == []


test_unique_elements()
# %%


def odd_elements(arr: list) -> list:
    # write your code here
    odd_list_ = []
    for symbol in arr:
        a = arr.count(symbol)
        if a % 2 == 1 and (symbol in odd_list_) == False:
            odd_list_.append(symbol)
    return odd_list_


def test_odd_elements():
    result1 = odd_elements([1, 2, 3, 2, 4, 5, 5])
    assert result1 == [1, 3, 4]
    result1 = odd_elements([1, 2, 3, 2, 4, 5, 5, 6, 6, 6])
    assert result1 == [1, 3, 4, 6]


test_odd_elements()

# %%


def second_largest_element(arr: list) -> int:
    if len(set(arr)) > 2:
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
        return arr[-2]
    else:
        return None


def test_second_largest_element():
    result1 = second_largest_element([1, 2, 3, 2, 4, 5, 5])
    assert result1 == 5
    result2 = second_largest_element([1, 2, 3, 4, 5])
    assert result2 == 4
    result3 = second_largest_element([1, 1, 1, 1, 1])
    assert result3 == None


test_second_largest_element()
# %%


def loop(arr: list, new_list: list, i):
    new_new_list = []
    for j in range(i, len(arr)-1):
        if arr[j] < arr[j+1]:
            new_new_list = new_list.append(arr[j+1])
    return new_new_list


def longest_increasing_sequence(arr: list) -> int:
    for i in range(len(arr)):
        new_list = [arr[i]]
        loop(arr, new_list, i)
    return new_list


def test_sum_of_two():
    result1 = longest_increasing_sequence([9, 9, 4, 2])
    assert result1 == 1
    result2 = longest_increasing_sequence(
        [10, 22, 9, 33, 21, 50, 41, 60, 22, 68, 90])
    assert result2 == 7
    result3 = longest_increasing_sequence([4, 3, 5, 1, 6])
    assert result3 == 3


print(longest_increasing_sequence([10, 22, 9, 33, 21, 50, 41, 60, 22, 68, 90]))
# %%
list_of_cities = [
    ('New York City', 8_550_405),
    ('Los Angeles', 3_792_621),
    ('Chicago', 2_695_598),
    ('Houston', 2_100_263),
    ('Philadelphia', 1_526_006),
    ('Phoenix', 1_445_632),
    ('San Antonio', 1_327_407),
    ('San Diego', 1_307_402),
    ('Dallas', 1_197_816),
    ('San Jose', 945_942),
]
sorted_list = sorted(list_of_cities, key=lambda x: x[1])
total_pop = 0
average_pop = 0
for i in range(len(sorted_list)):
    total_pop += sorted_list[i][1]
average_pop = round(total_pop / len(list_of_cities), 100)
print(total_pop, average_pop)
