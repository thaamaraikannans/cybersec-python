# import basic
# from basic import multiply, divide, subtract
from basic import * 
import extra
import sqlalchemy

def main():
    response = multiply(10, 20)
    # response = divide()
    # response =add1()
    # response = subtract()
    print(response)
    extra.integral()
    print("mysql alchemy version", sqlalchemy.__version__)
    return

main()

# PIP