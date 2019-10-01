from configparser import ConfigParser
import os
folder ='C:\\RD'
config = ConfigParser()
numbers=(8,9,25)
for root,dirs,files in os.walk(folder):
    for file in files:
            with open(os.path.join(root,'VisualOCR.txt'),'r') as f:
                text=f.read()
            if  'ï»¿' in text :
                text=text.replace('ï»¿','')
            with open('text.txt','w') as f:
                f.write(text)
            config.read('text.txt')
            for i in numbers:
                k=0
                if config.has_option('Data', '{}'.format(i)) == True:
                    data=config.get("Data", '{}'.format(i))
                    fil=open('{0}.txt'.format(i),'a+')

                    fil.seek(0)
                    for line in fil:
                        if line == (data+'\n') or line == (data):
                            k+=1

                    if k == 0:
                        fil.write(data+ '\n')
                        fil.close()

os.remove('text.txt')
