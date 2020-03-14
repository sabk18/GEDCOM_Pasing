#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 22:07:37 2020

@author: sabkhalid
"""

import unittest
import datetime
from datetime import datetime, timedelta

class Death_Birth_DateValidator(unittest.TestCase):

    def test_for_same6(self):
        #result = testDates(datetime.now() - timedelta(days=1))
        self.assertFalse(testDates(datetime.now(), datetime.now()))

    def test_for_less6(self):
        result = testDates(datetime.now(), datetime.now() - timedelta(days=1))
        self.assertFalse(result)

    def test_for_more6(self):
        result = testDates(datetime.now(), datetime.now())
        self.assertTrue(result)

    def test_is_False6(self):
        result = testDates(datetime.now() + timedelta(days=15), datetime.now())
        self.assertFalse(result)
        
    def test_is_datetime6(self):
        result = testDates(datetime.now() - timedelta(days=15))
        self.assertFalse(result, datetime.now())


def testDates(input_date):

    input_date = datetime.strptime(input_date, '%d %b %Y')
    currentDate =datetime.now()
    if input_date <= currentDate:
        return True
    else:
        return False


def h6test(info, file):
    for indiv in info['INDI']:
        birth_date= info['INDI'][indiv]['BIRT']
        if 'DEAT' in info['INDI']:
            death_date= info['INDI'][indiv]['DEAT']
            if not testDates(death_date):
                file.write("Error at DEAT Date at INDI ID {0} ".format(indiv))
        if not testDates(birth_date):
            file.write("Error at Birth DATEat INDI ID{0}".format(indiv))


    for fam in info['FAM']:
        if 'MARR' in info['FAM'][fam]:
            marriage_date= info['FAM'][fam]['MARR']
            if not testDates(marriage_date):
                file.write("Error at MARR Date at FAM ID {0}".format(fam))
        if 'DIV'in info ['FAM'][fam]:
            divorce_date= info['FAM'][fam]['DIV']
            if not testDates(divorce_date):
                file.write("Error at DIV Date at FAM ID {0}".format(fam))
    return file

if __name__ == '__main__':
    unittest.main()        
