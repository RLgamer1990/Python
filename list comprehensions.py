users = [
    {
        'name': 'shai',
        'age': 30,
        'hobbies': ['Drink', 'Drive', 'Something!']
    },
    {
        'name': 'ido',
        'age': 31,
        'hobbies': ['Books', 'Weed']
    },
    {
        'name': 'Gilad',
        'age': 32,
        'hobbies': []
    }
]

# el - manipulation of an item -- for -- el -- in list - the list that is used -- after that u can add an if, etc.
user_over_30 = [item for item in users if item['age'] > 30]
# print(user_over_30)

# [first, ssecond, third] = users
# print(first)
#
#
user_with_hobbies_over_30 = [el['hobbies'] for el in users if el['age'] > 30 and len(el['hobbies']) > 0]
print(user_with_hobbies_over_30)
#
#
# # print(users)
# # users = a
# users2 = users
# # b=a
# users2 = []
# # print(users2 = []) - will return empty users list
#
# users2_deep_copy = [el for el in users]
# users2_deep_copy.append( {
#         'name': 'Tom',
#         'age': 33,
#         'hobbies': ['Drink', 'Drive', 'Something!']
#     },)
#
# print(users)
# print(users2_deep_copy)

