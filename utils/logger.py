import logging


logging.basicConfig(
    filename='debug.log',
    filemode='w',
    format='%(asctime)s %(levelname)s\n%(message)s\n\n',
    datefmt='%m/%d/%Y %I:%M:%S %p',
    level=logging.WARNING
)
logger = logging.getLogger(__name__)
