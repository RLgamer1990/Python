user_number = input('Pick a number:')
list = [5, 32, -5, 79, 14, 0, 11, 42, 38, 15, 3, 88, 25]
list2 = list

print(list2)


def calculate_even(numbers):
    even_sum = 0
    for num in numbers:
        if int(num) % 2 == 0:
            even_sum = even_sum + int(num)
            print('even number', num)
    return even_sum

def find_user_number():
    found_num = {
        "result": f'{user_number} Not found!',
        "match": False
    }
    for num in list:
        if num == int(user_number):
            found_num["result"] = num
            found_num["match"] = True
    return found_num

test = find_user_number()
print(f'This is your number {test["result"]}')
