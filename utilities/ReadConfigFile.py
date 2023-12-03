import configparser

# RawConfigParser will use to read the config.ini file
config = configparser.RawConfigParser()

config.read(r"F:\Testing Documents\Pycharm Practice\OrangeHRMFramework\Configuration\config.ini")


class ReadValue():

    @staticmethod
    def getUsername():
        username = config.get('login info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('login info', 'password')
        return password

    @staticmethod
    def getURL():
        url = config.get('login info', 'url')
        return url


