#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 16:54:26 2020

@author: sabkhalid
"""

import unittest


class Orphan_Check(unittest.TestCase):
    def test_death_husb_wife_true(self):
        result = death_check(['27 March 2018','14 April 2019'])
        self.assertTrue(result, 'True')
    def test_death_husb_wife_false(self):
        result = death_check(['x'])
        self.assertFalse(result, 'False')
    def test_age_check_true(self):
        result = age_check(15)
        self.assertTrue(result, 'True')
    def test_age_check_false(self):
        result = age_check(27)
        self.assertFalse(result, 'False')
        
        
#List all orphaned children (both parents dead and child < 18 years old) in a GEDCOM file
def death_check(fam_list):
    if len(fam_list) == 2:
        return True
    else:
        return False
    
def age_check(child_age):
    if child_age < 18:
        return True
    else:
        return False


def s33_test(info, file):
    for fam in info['FAM']:
        hus = info['FAM'][fam]['HUSB']
        wife = info['FAM'][fam]['WIFE']
        
        
        empty_list =[]
        if 'DEAT' in info['INDI'][hus]:
            husdeath_status = info['INDI'][hus]['DEAT']
            empty_list.append(husdeath_status)
        
        if 'DEAT' in info['INDI'][wife]:
            wifedeath_status = info['INDI'][wife]['DEAT']
            empty_list.append(wifedeath_status)
            
        #print (empty_list)
        
        if death_check(empty_list):
            if 'CHIL' in info['FAM'][fam]:                
                children_ids = info['FAM'][fam]['CHIL']
                for child in children_ids:
                    children_age = info['INDI'][child]['AGE']
                    if age_check(children_age):
                        child_name = info['INDI'][child]['NAME']
                        file.write("\n Child : {} is an orphan".format(child_name))
                    
                
    return file

        
        
if __name__ == '__main__':
    unittest.main()       
    
    
    