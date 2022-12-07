import logging


#logging.basicConfig(filename="CISCO-SB009.log", level=logging.NOTSET)
#logging.basicConfig(filename="CISCO-SB009.log", level=logging.DEBUG)
#logging.basicConfig(filename="CISCO-SB009.log", level=logging.INFO) # from 20 to 50
logging.basicConfig(filename="CISCO-SB009.log", level=logging.WARNING) # from 20 to 50

logging.debug("I am debug Message 1")
logging.debug("I am debug Message 2")
logging.debug("I am debug Message 3")

logging.info("I am Info Message 1")
logging.info("I am Info Message 2")
logging.info("I am Info Message 3")

logging.warning("I am Warning Message 1")
logging.warning("I am Warning Message 2")
logging.warning("I am Warning Message 3")

logging.error("I am Error Message 1")
logging.error("I am Error Message 2")
logging.error("I am Error Message 3")

logging.critical("I am Critical Message 1")
logging.critical("I am Critical Message 2")
logging.critical("I am Critical Message 3")



