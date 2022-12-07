import logging

logging.basicConfig(filename="Division.log", level=logging.DEBUG)

logging.info("START: Division Program")
try:
    x = int(input("Enter First Number : "))
    y = int(input("Enter Second Number : "))
    logging.info( x)
    logging.info( y)
    print(x/y)
except ZeroDivisionError as msg:
    logging.error("Can not be devided by ZERO")
    logging.exception(msg)
except ValueError as msg:
    logging.error("User not provided  Int Value ")
    logging.exception(msg)
logging.info("END: Division Program")
print("END: Division Program")



