# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 00:24:13 2017

@author: howtodowtle
"""

import gorgireader
import gorgimessages
import opslaget

# set values:

# only define path when different than 
# D:/Dropbox/Egmont/Regnskab/Aktuelt Regnskab/gangregnskab_egmontgl8.xlsx
df = gorgireader.getWorkbook()
month = "juli"
year = "2017"
# dates format: "2/7/2017-2/8/2017", or however you would like it to look
dates = "2/7/2017-2/8/2017"
deadline = "17/8"

# so far only printing, should also be saved in future
# create fb posting
opslaget.createOpslagetDK(month, year, dates)

# create messages
gorgimessages.createAllMessages(df, month, year, dates, deadline)