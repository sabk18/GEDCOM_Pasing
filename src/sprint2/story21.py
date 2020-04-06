#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Shivani Taneja
"""

import unittest


class CorrectGenderForRoleValidator(unittest.TestCase):

    def test_check_husband_gender(self):
        self.assertTrue(is_male_gender('M'))

    def test_check_wife_gender(self):
        self.assertTrue(is_female_gender('F'))

    def test_check_husband_gender_another(self):
        self.assertFalse(is_male_gender('F'))

    def test_check_wife_gender_another(self):
        self.assertFalse(is_female_gender('M'))


def is_male_gender(gender):
    if not isinstance(gender, str):
        return False

    if gender == 'M':
        return True

    return False


def is_female_gender(gender):
    if not isinstance(gender, str):
        return False

    if gender == 'F':
        return True

    return False


def s21_test(info, file):
    # This has been implemented for each family
    for fam in info['FAM']:
        husband_id = info['FAM'][fam]['HUSB']
        wife_id = info['FAM'][fam]['WIFE']

        husband_gender = info['INDI'][husband_id]['SEX']
        wife_gender = info['INDI'][wife_id]['SEX']

        if not is_male_gender(husband_gender):
            file.write("\n{0} family does not have correct gender for husband".format(fam))

        if not is_female_gender(wife_gender):
            file.write("\n{0} family does not have correct gender for wife".format(fam))

    return file


if __name__ == '__main__':
    unittest.main()
