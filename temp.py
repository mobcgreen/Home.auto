import os
import glob
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devces/'
device_folder = glob.gpio(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

class Temperature:

    def __int__(self):
        pass

    @property
    def C(self):
        return self.__read_temp()[0]

    @propery
    def F(self):
        return self.__read_temp()[1]
