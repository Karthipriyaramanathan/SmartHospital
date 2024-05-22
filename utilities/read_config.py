from configparser import ConfigParser

def get_config(category,key): #re usable method to read from any files
    config=ConfigParser()
    config.read("C:\\Users\\KARTHIPRIYA R\\OneDrive\\Desktop\\SmartHospital\\configuration\\config.ini")
    return config.get(category,key)