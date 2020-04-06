#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: shivanitaneja
"""

import unittest
import datetime
from datetime import datetime
from datetime import date


class LivingAbove30AndNotMarriedPeopleValidator(unittest.TestCase):

    def test_for_type_living_and_over_30(self):
        self.assertFalse(is_individual_living_and_over_30("Beer", '@12344@'))

    def test_for_type_married(self):
        self.assertFalse(is_individual_married([1, 2, 3], '@9876'))

    def test_for_individual_living_below_30(self):
        self.assertFalse(is_individual_living_and_over_30({'INDI': {'@I6000123@': {'NAME': 'Himanshu', 'SEX': 'M',
                                                                                   'BIRT': '26 MAY 2010'}}},
                                                          '@I6000123@'))

    def test_for_individual_living_above_30(self):
        self.assertTrue(is_individual_living_and_over_30({'INDI': {'@I8098234@': {'NAME': 'Taau Ji',
                                                                                  'SEX': 'M', 'BIRT': '26 AUG 1980'}}},
                                                         '@I8098234@'))

    def test_for_individual_died(self):
        self.assertFalse(is_individual_living_and_over_30({'INDI': {'@I8098234@': {'NAME': 'Taau Ji',
                                                                                   'SEX': 'M', 'DEAT': '9 FEB 1993',
                                                                                   'BIRT': '26 MAY 1918'}}},
                                                          '@I8098234@'))

    def test_for_individual_married(self):
        self.assertTrue(is_individual_married({'INDI': {'@I4553123@': {'NAME': 'Himanshu Dagar',
                                                                       'SEX': 'M', 'FAMS': '@F2342@'}}},
                                              '@I4553123@'))

    def test_for_individual_married_another(self):
        self.assertFalse(is_individual_married({'INDI': {'@I1789876@': {'NAME': 'Taai Ji',
                                                                        'SEX': 'F', 'DEAT': '9 FEB 1993'}}},
                                               '@I1789876@'))


def is_individual_living_and_over_30(info, indiv_id):
    if not isinstance(info, dict) or not isinstance(indiv_id, str):
        return False

    if 'INDI' not in info:
        return False

    if indiv_id not in info['INDI']:
        return False

    if 'BIRT' not in info['INDI'][indiv_id]:
        return False

    birth_date_str = info['INDI'][indiv_id]['BIRT']
    birth_date_obj = datetime.strptime(birth_date_str, '%d %b %Y')
    age = (date.today().year - birth_date_obj.year - (
            (date.today().month, date.today().day) < (birth_date_obj.month, birth_date_obj.day))) + 1

    # success case
    if ('DEAT' not in info['INDI'][indiv_id]) and age > 30:
        return True

    return False


def is_individual_married(info, indiv_id):
    if not isinstance(info, dict) or not isinstance(indiv_id, str):
        return False

    if 'INDI' not in info:
        return False

    if indiv_id not in info['INDI']:
        return False

    if 'FAMS' in info['INDI'][indiv_id]:
        return True

    return False


def s31_test(info, file):
    # This has been implemented for each individual
    file.write("\nList of living people over 30 who have never been married is: [ \n")
    for indiv in info['INDI']:
        if is_individual_living_and_over_30(info, indiv) and (not is_individual_married(info, indiv)):
            file.write("{0} ({1}), \n".format(info['INDI'][indiv]['NAME'], indiv))

    file.write("]\n")
    return file


if __name__ == '__main__':
    unittest.main()
