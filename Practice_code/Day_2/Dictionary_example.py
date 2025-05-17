# creating a dictionary

products = {
 101: {"product_id": 1001, "product_name":"bottle", "quantity":200, "price": 10000},
 102: {"product_id": 1002, "product_name":"pen", "quantity":800, "price": 50000},
 103: {"product_id": 1003, "product_name":"tissue", "quantity":500, "price": 60000},
}

print("keys in the dict:",products.keys())

#values - returns a view of all the values in the dict
values = products.values()

#update
products.update({104: {"product_id": 1004, "product_name":"mobile", "quantity":10000, "price": 500000}})
                
#pop
removed_products = products.pop(102)

#popitem
last_products = products.popitem()

#clear
products.clear()

print("Values", values)
print("Removed products:", removed_products)
print("Last inserted products:", last_products)
print("after clear the products:", products)

#product name occurs or not
for i in products:
    if "product_name" == "tissue":
        print("Tissue is in the product")
    else:
        print("Tissue is not in the product")