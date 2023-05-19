import configparser
config = configparser.RawConfigParser()
config.read(".//Configuration//config.ini")


class readconfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getusername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getUser_Name():
        valid_username = config.get('common info', 'valid_username')
        return valid_username

    @staticmethod
    def getpassword():
        valid_password = config.get('common info', 'valid_password')
        return valid_password
