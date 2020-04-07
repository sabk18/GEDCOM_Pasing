pyder#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 2 14:00:42 2020

@author: sabkhalid
"""

#story 25: Unique first names in Family
#No more than one child with the same name and birth date should appear in the family
#step 1: for each row of FAM, chk for children id. for every unique children id, chk for their birth date in INDI. if unique then show that in
#family table.

import unittest


class Unique_birthDate_firstName(unittest.TestCase):
    def test_unique_childIDs_true(self):
        result = unique_childID(['xyz', 'abc','123'])
        self.assertTrue(result, 'True')
    def test_unique_childIDs_equal(self):
        result1 = unique_childID(['xyz', 'abc','123'])
        result2 = unique_childID(['xyz', 'abc','123'])
        self.assertEqual(result1, result2)
    def test_true_unique_FirstName_BirthDate(self):
        result = name_birth(['Meredith - 9th Feb 1995', 'Alex - 30th Jan 1998', 'Christina - 26th July 1990'])
        self.assertTrue(result, 'True')
    def test_false_unique_FirstName_BirthDate(self):
        result= name_birth(['Meredith - 9th Feb 1995', 'Alex - 30th Jan 1998', 'Meredith - 9th Feb 1995'])
        self.assertFalse(result, 'False')
    

def unique_childID(children):
    if len(children) == len(set(children)):  #chk if unique 
        return True
    else:
        return False
    
def name_birth(data):
    if len(data) == len(set(data)):
        return True
    else:
        return False
    
def s25test(info, file):
    for fam in info['FAM']:
        if 'CHIL' in info['FAM'][fam]:
            children_ids = info['FAM'][fam]['CHIL']
            if unique_childID(children_ids):
                uniqueChild = []
                for child in children_ids:
                    children_name = info['INDI'][child]['NAME']
                    name_split = children_name.split('/')
                    first_name = name_split[0]
                    #print (first_name)
                    date_of_birth = info['INDI'][child]['BIRT']
                    #print (date_of_birth)
                    child = first_name + ' - ' + date_of_birth            
                    uniqueChild.append(child)
                if not name_birth(uniqueChild):                    
                    file.write("\nError: For Family ID {}, there should be unique child first name and birth date".format(fam))
     
    return file
          
    
if __name__ == '__main__':
    unittest.main()    