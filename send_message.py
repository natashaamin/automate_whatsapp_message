import pywhatkit as pwt
import pandas as pd
import numpy as np
import pyautogui as pg
from datetime import datetime

df = pd.DataFrame()
countryCode = '+60'
phoneNumber = ''
message = 'Assalamualaikum/Hello '
message1 = 'For our reception at Regelia ball, we have reserved seats for you at '
message2 = 'We look forward to welcoming you. \nBy Amins Family'
now = datetime.now()
hour = int(now.strftime("%H"))
minute = int(now.strftime("%M"))

path = ('/Users/natasha.s.binti.amin/Downloads/copy.csv')
dataset = pd.read_csv(path, usecols= ['Name','Table', 'Number'])
number = dataset.iloc[:,2].values.tolist()

for x in number:
    if not (np.isnan(x)):
        result_df = dataset.query("Number == @x")
        for i in range(len(result_df)):
            minute += 1
            finalMessage = message + result_df['Name'].iloc[i] + '\n\n' + message1 + result_df['Table'].iloc[i] + '\n\n' + message2
            phoneNumber = (countryCode + str(x))[:-2]
            pwt.sendwhatmsg(phoneNumber, finalMessage, hour, minute, 40, True, 5)
