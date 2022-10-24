import uuid

# if repository is empty user has to input products
repository = [{
    'id': 1,
    'name': 'chair',
    'price': 100,
},
    {
        'id': 2,
        'name': 'table',
        'price': 300,
    },
    {
        'id': 3,
        'name': 'computer',
        'price': 3000,
    }
]
app_status = True


def get_repository():
    print(f"this is your product list {repository}")


def new_product():
    print('--Creating a new product--')
    product_name = input('Please enter product name:')
    product_price = int(input('please enter product price:'))
    # Class
    u_id = uuid.uuid4()
    product = {
        'id': u_id,
        'name': product_name,
        'price': product_price,
    }
    repository.append(product)


def update_price():
    print('--Update new price--')
    prod_name = input('product for update:')
    price_value = int(input('please enter new price:'))
# current price is just to have a starting point for comparing between lists
    current_price = 0

    for pr in repository:
        if pr['name'] == prod_name:
            current_price = pr['price']
            pr['price'] = price_value

    if price_value != current_price:
        print('Price was changed!')
    else:
        print('Nothing to do with that!')


def delete_product():
    global repository
    current_len = len(repository)
    print('--choose product to delete--')
    prod_name = input('choose a product to delete:')
    new_repository = [el for el in repository if prod_name != el['name']]
    repository = new_repository
    new_len = len(new_repository)

    if new_len == current_len:
        print('Nothing happens')
    else:
        print('product has been deleted!')


# will delete a specific property in a dict
# del obj name(dict property)


def shut_down():
    global app_status
    app_status = False


while app_status:
    print("1. Fetch all products")
    print("2. Create new product")
    print("3. Update product price")
    print("4. Delete product by name")
    print("5. Quit")
    user_input = input("User Choice:")

    if user_input == "1":
        get_repository()
    if user_input == "2":
        new_product()
    if user_input == "3":
        update_price()
    if user_input == "4":
        delete_product()
    if user_input == "5":
        shut_down()

print('Done!')
