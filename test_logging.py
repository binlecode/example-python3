
# python 3 basic logging tutorial: https://docs.python.org/3/howto/logging.html

import logging
import os

os.system("echo '' > test_logging.log")

logging.basicConfig(filename='test_logging.log',level=logging.DEBUG)

logging.debug('this is a debug level message')
logger = logging.getLogger()
logger.debug('this is debug msg from logger')
logger.setLevel(logging.INFO)
logger.debug('this is debug msg from logger')  # won't print since DEBUG < INFO level
logger.info('this is info msg from logger')


# load logging config from file, which is more common for application coding

from logging.config import fileConfig

fileConfig('test_logging_config.ini')
logger = logging.getLogger()
logger.debug('hard to see through %s is', 'the future')
