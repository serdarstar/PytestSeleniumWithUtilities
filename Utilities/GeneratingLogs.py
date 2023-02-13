import logging


def log():
    logging.basicConfig(filename="..\\Logs\\logfile.log", format='%(asctime)s: %(levelname)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p'
                        , level=logging.INFO)
    logger = logging.getLogger()
    logger.info("This is first log")
    return logger


logger1 = log()
logger1.info("First log")
