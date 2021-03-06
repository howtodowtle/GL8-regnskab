# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 20:25:18 2017

@author: howtodowtle
"""
def whichMessage(df):
   # reads saldo
   # decides, which message to choose
   # returns an index
   
   # initiate a list of messages:
   # -1: negative (under 0 kr.)
   # 0: neutral (0-300 kr.)
   # 1: positive (over 300 kr.)
   choice = []
   # NB: with .ix accessing the index of the panda df, 
   # so not neccessarily starting at 0
   for i in range(1, 23):
       beboer = df.ix[i]
       if round(beboer["ny_saldo"]) < 0:
           choice.append(-1)
       elif round(beboer["ny_saldo"]) < 300:
           choice.append(0)
       else:
           choice.append(1)
   
   # add the decision as an 8th col [index 7] to the dataframe
   df["msg_type"] = choice        
   return(df)

# df = whichMessage(df)

def createMessage(name, month, year, dates, saldo, 
                  transfer, deadline, decision = 1):
    # creates a single message
    if round(saldo) < 0:
        message = ("Hej %s,\n\nregnskabet for %s %s (%s) er oppe i facebook "
                   "gruppen.\n\nDin nye saldo er %d kr.\n\nDa alle skal være "
                   "mindst 300 kr. i plus bedes du overføre %d kr. til "
                   "gangkontoen inden d. %s.\n\nSkriv til mig hvis jeg har "
                   "glemt et eller andet, og hvis du har spørgsmål!\n\nKh "
                   "/801 Alex\n\nGangkonto: Reg. 2104 Kto. 4391 845 196"
                   % (name, month, year, dates, round(saldo), 
                      round(transfer), deadline))
    elif round(saldo) < 300:
        message = ("Hej %s,\n\nregnskabet for %s %s "
                   "(%s) er oppe i facebook gruppen.\n\nDin "
                   "nye saldo er +%d kr.\n\nDa alle skal være mindst 300 kr. "
                   "i plus bedes du overføre %d kr. til gangkontoen inden d. "
                   "%s.\n\nSkriv til mig hvis jeg har glemt et eller andet, "
                   "eller hvis du har spørgsmål!\n\nKh /801 Alex\n\n"
                   "Gangkonto: Reg. 2104 Kto. 4391 845 196"
                   % (name, month, year, dates, round(saldo), 
                      round(transfer), deadline))
    else:
        message = ("Hej %s,\n\nregnskabet for %s %s "
                   "(%s) er oppe i facebook gruppen.\n\nDin "
                   "nye saldo er +%d kr.\n\nDu kan se detaljerne på de "
                   "forskellige screenshots i gruppen.\n\nSkriv til mig "
                   "hvis jeg har glemt et eller andet, og hvis du har "
                   "spørgsmål!\n\n/801 Alex\n\nGangkonto: Reg. 2104 Kto. "
                   "4391 845 196"
                   % (name, month, year, dates, round(saldo)))
        
    return(message)

#m1 = createMessage("alex", "juni", "2017", "somedates", 12, 288, "deeead", 1)    
    
def createAllMessages(df, month, year, dates, deadline, who = range(1, 23)):
    # goes through the dataframe and creates 23 messages
    # unless specified which exactly
    messages = []
    for i in who:
        beboer = df.ix[i]
        msg = createMessage(beboer["name"], month, year, dates,
                            beboer["ny_saldo"], beboer["transfer"],
                            deadline)
        messages.append(msg)
        print(msg)
        print("\n****\n")
    return(messages)