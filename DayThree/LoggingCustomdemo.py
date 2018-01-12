import logging

emc_logger = logging.getLogger('emc')
emc_logger.setLevel(logging.DEBUG)

frm_str = "%(asctime)s:%(levelname)s:%(name)s:%(process)s:%(message)s"
formtr = logging.Formatter(frm_str)
streamhandle = logging.StreamHandler()
filehandler = logging.FileHandler('custom.log')

streamhandle.setFormatter(formtr)
filehandler.setFormatter(formtr)

emc_logger.addHandler(streamhandle)
emc_logger.addHandler(filehandler)

emc_logger.debug('HI all')
