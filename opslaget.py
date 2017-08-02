# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 19:37:35 2017

@author: howtodowtle
"""
#row_in_array, index, dates,
def createOpslagetEN(monthEN, year, dates):
    # creates a facebook post
    # in ENglish
    posting = ("GANGREGNSKAB %s % (%s)\n\n"    
    "Hej venner!\n\n"
    "The new kitchen balances are up in the Facebook group!\n\n"
    "Check your new saldo in the green column. If the saldo "
    "is below +300 kr., you are supposed to transfer money "
    "to the kitchen account (information see below). How much "
    "you are supposed to transfer can be seen in the column right next to "
    "the green column.\n\n"
    "There is also a summary of your consumption in the last month that "
    "can be seen in the second picture. Your monthly consumption is "
    "composed of a possible penalty tax (if your saldo is negative and "
    "you haven't settled it), your beer bill (from the common fridge), your "
    "foodclub saldo (both what you ate for and what you spent cooking), "
    "25 kr. kitchen tax, your share of our common purchases. Plus/minus "
    "400 kr. deposit when moving in/out.\n\n"
    "Mit freundlichen Grüßen\n"
    "/801.\n\n"
    "Our kitchen account: Reg. 2104 Kto. 4391 845 196 (can also be found "
    "in the facebook group info)." 
    % (monthEN, year, dates))

    return(print(posting))

def createOpslagetDK(monthDK, year, dates):
    # creates a facebook post
    # in DK (Danish)
    opslag = ("GANGREGNSKAB %s %s (%s)\n\n"
    "Hej venner,\n\n"
    "det nye gangregnskab er oppe!\n\n"
    "Tjek jeres ny saldo i den grøn kolonne. Hvis saldoen er under 300 kr. "
    "så skal i overføre til gangkontoen i løbet af to uger (ellers ryger der "
    "5 procent strafrente). Beløbet i skal overføre står i kolonnen "
    "helt til højre.\n\n"
    "Mit freundlichen Grüßen\n"
    "/801.\n\n"
    "Vores gangkonto: Reg. 2104 Kto. 4391 845 196 (kan også findes i "
    "informationen af facebook gruppen)."
    % (monthDK, year, dates))

    return(print(opslag))    
    