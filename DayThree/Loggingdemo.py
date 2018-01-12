import logging

frm_str = "%(asctime)s:%(levelname)s:%(name)s:%(process)s:%(message)s"
logging.basicConfig(level=logging.DEBUG, filename='access.log', format=frm_str)
logging.debug('debug msg')
logging.info('Info Messgae')
logging.critical('this is critical')
logging.warning('Hi this is warning')