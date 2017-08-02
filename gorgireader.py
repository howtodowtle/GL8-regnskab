# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 20:25:18 2017

@author: howtodowtle
"""
# import xlrd
import pandas as pd
import numpy as np

def getWorkbook(path = "D:/Dropbox/Egmont/Regnskab/Aktuelt Regnskab/", 
                    filename = "gangregnskab_egmontgl8.xlsx"):
    
    # Get excel workbook and select the appropriate sheet
    regnskab = pd.read_excel(path + filename, sheet_name = "Regnskab")
    
    # extract the relevant part (current inhabitants and overview data)
    regnskab = regnskab.ix[2:24, :7]
    
    # rename columns
    regnskab.columns = ["nummer", "name", "gammel_saldo", "ind", "forbrug",
                        "ny_saldo", "transfer"]
    
    # reset the indices (rownames): 1 to 23
    regnskab.index = range(1, 24)
    
    # return the dataframe
    return(regnskab)

#df = getWorkbook()




