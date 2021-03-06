import inspect
import logging

class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)  # this object is responsible for all logging - the name returns test name
        fileHandler = logging.FileHandler('logfile.log')  # say the file location and name
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # must pass in a filehandler object (which is just the file location)

        logger.setLevel(
            logging.DEBUG)  # this level is in order DEBUG\INFO\WARN\ERROR\CRITICAL and will show only logs above set level

        return logger