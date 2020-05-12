import logging


def get_logger(logr_name):
    # create logger
    logger = logging.getLogger(logr_name)
    logger.setLevel(logging.DEBUG)

    # create file handler which logs the messages into a file
    fh = logging.FileHandler('logFile.log')
    fh.setLevel(logging.DEBUG)

    # create console handler which logs the messages to console
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger