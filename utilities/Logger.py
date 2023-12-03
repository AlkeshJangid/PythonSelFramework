import logging
import inspect
class LogGen:

    @staticmethod
    def loggen():
        classname = inspect.stack()[1][3]
        logger = logging.getLogger(classname)  #<<- ye logger file lekar aa rahe hai
        # or har ek activity ke bad
        # niche vali file path se
        file = logging.FileHandler(r"F:\Testing Documents\Pycharm Practice\OrangeHRMFramework\Logs\logfile.log")
        # iss format me data
        format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(message)s")
        # yaha store krne ka kaam karegi
        file.setFormatter(format)
        #or hamasha logger ka Data issi file me commit ho, uske liye addHandler krke object use karenge
        logger.addHandler(file)

        logger.setLevel(logging.INFO)
        return logger

