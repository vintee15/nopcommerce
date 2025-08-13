import configparser
import os
# configparser is package & inside this RawConfigParser is class
config = configparser.RawConfigParser() # create object
# config.read(".\\Configurations\\config.ini") #to read values
file_path = os.path.join(os.getcwd(), "Configurations", "config.ini")
# print("Reading config from:", file_path)
config.read(file_path)

# to get value from .ini file create a class (ReadConfig)

class ReadConfig:       #it is python file
# for every variable in .ini file, we need to create one method
    @staticmethod    #make getApplicationURL static because static method can directly call using class name. no nead to create object
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url


    @staticmethod
    def getUseremail():
        username = config.get('common info', 'useremail')   #read value from .ini file
        return username    


    @staticmethod

    def getPassword():
        password = config.get('common info', 'password')
        return password



