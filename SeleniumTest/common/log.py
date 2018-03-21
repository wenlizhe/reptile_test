import calendar
import logging.handlers

CRITICAL = 50
ERROR = 40
WARNING = 30
INFO = 20
DEBUG = 10
NOTSET = 0


class Logger(object):

    def __init__(self, log_file='test_log.txt', level=NOTSET):
        self.logger = None

        self.levels = {"n": logging.NOTSET,
                       "d": logging.DEBUG,
                       "i": logging.INFO,
                       "w": logging.WARN,
                       "e": logging.ERROR,
                       "c": logging.CRITICAL}

        self.log_level = "d"
        self.log_file = log_file
        self.log_max_byte = 10 * 1024 * 1024
        self.log_backup_count = 5

    def get_logger(self):
        if self.logger is not None:
            return self.logger

        self.logger = logging.Logger("")
        log_handler = logging.handlers.RotatingFileHandler(filename=self.log_file,
                                                           maxBytes=self.log_max_byte,
                                                           backupCount=self.log_backup_count)
        log_fmt = logging.Formatter("[%(levelname)s][%(funcName)s][%(asctime)s]%(message)s")
        log_handler.setFormatter(log_fmt)
        self.logger.addHandler(log_handler)
        self.logger.setLevel(self.levels.get(self.log_level))
        return self.logger


class Log(object):
    def log(message, level=NOTSET):
        """
        向JusAuto传递日志
        :param message: 日志消息
        :param level: 日志级别，取值CRITICAL, ERROR, WARNING, INFO, DEBUG, NOTSET
        :return: 无
        """
        if level in (CRITICAL, ERROR, WARNING, INFO, DEBUG, NOTSET):
            obj_log = {'log': self.get_log_message_object(message, level)}
            print(json.dumps(obj_log))
            sys.stdout.flush()
        else:
            self._value_not_in_range_syntax_error('level')

    def get_log_message_object(self, message, level=NOTSET):
        return _create_object(message=message, level=level)

    def _create_object(self, **kwargs):
        kwargs['time'] = calendar.timegm(time.gmtime())
        return kwargs


if __name__ == "__main__":
    lo = Logger()
    logger = lo.get_logger()
    logger.debug("this is a debug msg!")
    logger.info("this is a info msg!")
    logger.warning("this is a warn msg!")
    logger.error("this is a error msg!")
    logger.critical("this is a critical msg!")
