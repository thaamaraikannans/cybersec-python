import re

pattern = r"^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\D{2,3})+$"

value = "kannan_s@gmail.cs"

final = re.match(pattern, value)

print(final)




# sql queries --- they uses escape character -> they do sql injection

# we need verify that weather do we have any escape character in our sql query