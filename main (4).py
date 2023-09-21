def linear_search_product(product_list, target_product_name):
    indices = []
    for index, product in enumerate(product_list):
        if product["name"] == target_product_name:
            indices.append(index)
    return indices
# Sample list of products (list of dictionaries)
products = [
    {"name": "Laptop", "price": 800},
    {"name": "Phone", "price": 500},
    {"name": "Tablet", "price": 300},
    {"name": "Laptop", "price": 900},
    {"name": "Laptop", "price": 850},
]

target_product_name = "Laptop"

# Call the linear_search_product function
result_indices = linear_search_product(products, target_product_name)

# Print the indices of the target product
if result_indices:
    print(f"The target product '{target_product_name}' was found at indices: {result_indices}")
else:
    print(f"The target product '{target_product_name}' was not found in the list.")