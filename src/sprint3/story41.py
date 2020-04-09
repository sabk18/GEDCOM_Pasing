#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 22:18:31 2020

@author: sabkhalid
"""

#story41: include partial dates. 'Only Year '

from datetime import *

def partial_date(date):
    try:        
        date_dt = datetime.strptime(date, '%d %b %Y') #change to datetime
        Year = date_dt.year
    except:
        False
    return Year
        
def s41test(info, file):
    
    for indiv in info['INDI']:  
        if 'BIRT' in info['INDI'][indiv]:           
            birth_date= info['INDI'][indiv]['BIRT']
            birth_date = partial_date(birth_date)
            print("\nINDI: {} ".format(indiv) , "Partial Birth Date: {}".format(birth_date))
        
                       
        if 'DEAT' in info['INDI'][indiv]: 
            death_date = info['INDI'][indiv]['DEAT']
            death_date = partial_date(death_date)
            print("\nINDI: {} ".format(indiv) , "Partial Death Date: {}".format(death_date))
       
    for fam in info['FAM']:
        if 'MARR' in info['FAM'][fam]:
            marriage_date= info['FAM'][fam]['MARR']
            marriage_date = partial_date(marriage_date)
            print("\nINDI: {} ".format(indiv) , "Partial Marriage Date: {}".format(marriage_date))
        
        if 'DIV'in info ['FAM'][fam]:
            divorce_date= info['FAM'][fam]['DIV']
            divorce_date =partial_date(divorce_date)
            print("\nINDI: {} ".format(indiv) , "Partial Divorce Date: {}".format(divorce_date))
            
            
    return file 
