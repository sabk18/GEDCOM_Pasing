#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 15:06:48 2020

@author: sabkhalid
"""

import unittest
import datetime
from datetime import datetime,timedelta

class Death_Birth_DateValidator(unittest.TestCase):

    def test_for_same(self):
        result = testDates(datetime.now(), datetime.now())
        self.assertTrue(result)

    def test_for_less(self):
        result = testDates(datetime.now(), datetime.now() - timedelta(days=1))
        self.assertFalse(result)

    def test_for_more(self):
        result = testDates(datetime.now(), datetime.now() + timedelta(days=1))
        self.assertTrue(result)

    def test_is_False(self):
        result = testDates(datetime.now() + timedelta(days=15), datetime.now())
        self.assertFalse(result)
        
    def test_is_datetime(self):
        result = testDates('False','False')
        self.assertFalse(result)
    

def testDates(birth, death):

    if birth < death:
        return True
    else:
        return False
        
def s3test(info, file):
    for indiv in info['INDI']:  
        if 'BIRT' in info['INDI'][indiv] and 'DEAT' in info['INDI'][indiv]:            
            birth_date= info['INDI'][indiv]['BIRT']
            death_date = info['INDI'][indiv]['DEAT']
            if not testDates(birth_date, death_date):
                file.write('Issue with {0} Indivisual Birth and Death Dates\n '.format(indiv))
    return file

        
if __name__ == '__main__':
    unittest.main()        