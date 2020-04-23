#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 19:06:37 2020

@author: sabkhalid
"""


import unittest


class LastName_Check(unittest.TestCase):
    
    def test_male_gender_true(self):
        result = male_gender('M')
        self.assertTrue(result, 'True')
    def test_male_gender_false(self):
        result = male_gender('F')
        self.assertFalse(result, 'False')
    def test_last_name(self):
        result = last_name('meredith/Grey/')
        lastName = 'Grey'
        self.assertEqual(result, lastName)
    def test_last_name_false(self):
        result = last_name('meredith/Alex/')
        lastName = 'Grey'
        self.assertNotEqual(result, lastName)
        
    
def male_gender(child):
    if child == 'M':
        return True
    else:
        return False
    
def last_name(name):
    name_split = name.split('/')
    last_name = name_split[1]
    return last_name
    
    
def s16_test(info, file):
    for fam in info['FAM']:
        male = info['FAM'][fam]['HUSB']
        if 'NAME' in info['INDI'][male]:
            male_name = info['INDI'][male]['NAME']
            name_split = male_name.split('/')
            family_name = name_split[1]
        if 'CHIL' in info['FAM'][fam]: 
            children = info['FAM'][fam]['CHIL']
            for child in children:
                children_gender = info['INDI'][child]['SEX']
                if male_gender(children_gender):
                    child_name = info['INDI'][child]['NAME']
                    if last_name(child_name) != family_name:
                        file.write("\n Error. Last name of Male Child {} of family {} is not valid".format(child_name, fam))
                        
                    
        
    return file
if __name__ == '__main__':
    unittest.main()       
