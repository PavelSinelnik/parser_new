from configparser import ConfigParser
config = ConfigParser()
config.read("C:\RD\Capa Verde\ePassport (2015)\SAMPLE-0007\VisualOCR.txt",encoding = 'utf-8-sig')
data=config.get("Data", '4')
print(data)