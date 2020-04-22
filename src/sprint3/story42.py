#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 20:18:51 2020

@author: sabkhalid
"""


#story41: include partial dates. 'Only Year '

from datetime import *
import unittest


class Valid_Date_Chk(unittest.TestCase):
    def test_Valid_Date_true(self):
        result = valid_date("9 Feb 1993")
        self.assertTrue(result, "9 Feb 1993")
    def test_Invalid_Date(self):
        result =valid_date("30 Feb 1993")
        self.assertRaises(ValueError)

def valid_date(date):
    try:
        date = datetime.strptime('date', '%d %b %Y').date() #change to datetime
    except ValueError:
        False
    return date
    

def s42test(info, file):
    
    for indiv in info['INDI']:  
        if 'BIRT' in info['INDI'][indiv]:           
            birth_date= info['INDI'][indiv]['BIRT']
            birth_date = valid_date(birth_date)
            if not valid_date(birth_date):
                file.write("\nError: For INDI ID {}, there should be valid Birth date".format(indiv))
                
                                   
        if 'DEAT' in info['INDI'][indiv]: 
            death_date = info['INDI'][indiv]['DEAT']
            death_date = valid_date(death_date)
            if not valid_date(death_date):
                file.write("\nError: For INDI ID {}, there should be valid Death date".format(indiv))
                
    for fam in info['FAM']:
        if 'MARR' in info['FAM'][fam]:
            marriage_date= info['FAM'][fam]['MARR']
            marriage_date = valid_date(marriage_date)
            if not valid_date(marriage_date):
                file.write("\nError: For INDI ID {}, there should be valid marriage date".format(indiv))
            
        if 'DIV'in info ['FAM'][fam]:
            divorce_date= info['FAM'][fam]['DIV']
            divorce_date =valid_date(divorce_date)
            if not valid_date(divorce_date):
                file.write("\nError: For INDI ID {}, there should be valid Divorce date".format(indiv))
            
            
    return file

if __name__ == '__main__':
    unittest.main()    