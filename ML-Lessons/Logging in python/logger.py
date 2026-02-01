import logging


logging.basicConfig(
    
    filename='app.log',
    filemode='w',
    level= logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt= '%Y-%m-%d %h:"%m:%S'
)

# Log message with different severity level.
# We used different file for lo