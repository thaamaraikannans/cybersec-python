with open("main.txt", "r") as file:
    var1 = file.readlines()
    

for name in var1:
    unified_name = name.strip()
    # print(unified_name)
    with open(unified_name, "r") as content:
        print(f"The content stored in file : {unified_name}")
        print(content.read())
        print("-"*50)