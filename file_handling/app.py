# data = open("demo.txt", "r")
# print(data.read())

# file = open("index.html", "r+")
# file.write("\nKannan")
# file.close()


# data = open("kannan.html", "w")
# data.write("""
#            <html>
#            <body>
#            <center>
#            <h1> Hi from Python !!!</h1>
#            </center>
#            </body>
#            </html>
#            """)
# data.close()


# with open("index.html", "w") as file:
#     file.write("""
#            <html>
#            <body>
#            <center>
#            <h1> Hi from Python !!!</h1>
#            </center>
#            </body>
#            </html>
#            """)

# file1 = open("index.html", "r")
# reaad = file1.read()
# print(reaad)

# with open("index.html", "r") as file:
#     for line in file:
#         print(line.strip())


with open("index.html", "r") as file:
    readed = file.readlines()

print(readed)
print(type(readed))
print(len(readed))
print(readed[5])
readed.insert(-2, "\n<h2>i'm new to programming</h2>\n")
print(readed)

with open("index.html", "w") as random:
    random.writelines(readed)