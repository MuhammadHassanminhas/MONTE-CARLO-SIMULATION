import pandas as pd
import random 

def RANDOM(min_percent,max_percent):
    value =  random.uniform(min_percent , max_percent+1)
    return value
    

def HALF_DECADE(min_percent,max_percent , price,result):
    data_HALF_DECADE = []
    
    for i in range(1,(5*365)+1):
        value=RANDOM(min_percent , max_percent)
        new_value = (value/100)+result+price
       
        data_HALF_DECADE.append(new_value)
    return data_HALF_DECADE
        
def YEAR(min_percent,max_percent , price,result):
    data_YEAR = []
    for i in range(1,366):
        value = RANDOM(min_percent , max_percent)
        new_value = (value/100)+result+price
        data_YEAR.append(new_value)
    return data_YEAR
        
def MONTHS(min_percent,max_percent , price,result):
    data_MONTH = []
    for i in range(1,14):
        value = RANDOM(min_percent , max_percent)
        new_value = (value/100)+result+price
        data_MONTH.append(new_value)
        
    return data_MONTH

def DAY(min_percent,max_percent , price,result):
    data_DAY = []

    for i in range(1,25):
        value = RANDOM(min_percent , max_percent)
        new_value = (value/100)+result+price
        data_DAY.append(new_value)
    return data_DAY



