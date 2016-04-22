import logging


# default log format
default_fmt = logging.Formatter('[%(asctime)s] %(levelname)s '
                                '(%(process)d) %(name)s : %(message)s',
                                datefmt='%Y/%m/%d %H:%M:%S')

# setup root logger
logger = logging.getLogger()
default_handler = logging.StreamHandler()
default_handler.setFormatter(default_fmt)
default_handler.setLevel(logging.DEBUG)
logger.addHandler(default_handler)


def setFmt(fmt=default_fmt):
    global defaut_handler
    default_handler.setFormatter(fmt)


def setRootLevel(level):
    global logger
    logger.setLevel(level)
