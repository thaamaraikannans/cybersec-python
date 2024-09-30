# try:
#     var_1 = ["Kannan", "Arun", "Karthick"]
#     print(var_1[6])
#     # c = 10/a
    
# except Exception as err:
#     print(err)

# print("The program executed successfully")

try:
    a = 100/0
    print(a)
    print("logic ran successfully")
except Exception as error:
    print(error)
else: 
    print("move to next step of program")
# finally:
#     print("I always ran on everytime")