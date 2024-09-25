car_brands = ["Toyoto", "Suzuki", "Tesla", "Renault", "Hyundai", "Tata", "Mahindra", "Lamboghini", "Volkswagen", "Tata"]
car_brands.sort()

print(car_brands)
length_brands = len(car_brands)
# print(length_brands)

# indexing -->> which index your want to access -> starts with 0 -> forward ....

# reverse indexing -> -1
# print(car_brands)

user_input = input(f"Enter your index value from 0 to {length_brands-1} : ")

# print(type(user_input))

# data casting, Type conversion, Changing or converting Data type 
# change one data type to another data type --> str to number(int/float/complex)

changed_input = int(user_input)

print(car_brands[changed_input])

# print(car_brands[1])
# print(car_brands[-5])