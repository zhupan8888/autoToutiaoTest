import logging.handlers
import os
import time

BASE_ARITCAL_TITLE = "TestCase_{}".format(time.strftime("%H%M%S"))

BASE_PATH = os.path.dirname(os.path.abspath("__file__"))


def log_base_config():
    logger = logging.getLogger()
    logger.setLevel(level=logging.INFO)

    ls = logging.StreamHandler()
    lht = logging.handlers.TimedRotatingFileHandler(filename=BASE_PATH + "/log", when="might", interval=1,
                                                    backupCount=2)

    formatter = logging.Formatter(fmt="%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s")

    ls.setFormatter(formatter)
    lht.setFormatter(formatter)

    logger.addHandler(ls)
    logger.addHandler(lht)
