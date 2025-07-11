def add_product(products_list):
    new_product_name = input('Please input your product name: ')
    if new_product_name not in products_list:
        products_list.append(new_product_name)
    return products_list
