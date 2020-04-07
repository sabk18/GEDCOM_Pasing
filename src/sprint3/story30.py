
"""
@author: Shivani Taneja
"""

import unittest


class LivingMarriedPeopleValidator(unittest.TestCase):

    def test_for_type_living(self):
        self.assertFalse(is_individual_living("Beer", '@12344@'))

    def test_for_type_married(self):
        self.assertFalse(is_individual_married([1, 2, 3], '@9876'))

    def test_for_individual_living(self):
        self.assertTrue(is_individual_living({'INDI': {'@I6000123@': {'NAME': 'Dagar', 'SEX': 'M'}}},
                                             '@I6000123@'))

    def test_for_individual_living_another(self):
        self.assertFalse(is_individual_living({'INDI': {'@I8098234@': {'NAME': 'Taau Ji',
                                                                       'SEX' : 'M', 'DEAT': '9 FEB 1993'}}},
                                              '@I8098234@'))

    def test_for_individual_married(self):
        self.assertTrue(is_individual_married({'INDI': {'@I4553123@': {'NAME': 'Dagar',
                                                                       'SEX' : 'M', 'FAMS': '@F2342@'}}},
                                              '@I4553123@'))

    def test_for_individual_married_another(self):
        self.assertFalse(is_individual_married({'INDI': {'@I1789876@': {'NAME': 'Taai Ji',
                                                                        'SEX' : 'F', 'DEAT': '9 FEB 1993'}}},
                                               '@I1789876@'))


def is_individual_living(info, indiv_id):
    if not isinstance(info, dict) or not isinstance(indiv_id, str):
        return False

    if 'INDI' not in info:
        return False

    if indiv_id not in info['INDI']:
        return False

    # success case
    if 'DEAT' not in info['INDI'][indiv_id]:
        return True

    return False


def is_individual_married(info, indiv_id):
    if not isinstance(info, dict) or not isinstance(indiv_id, str):
        return False

    if 'INDI' not in info:
        return False

    if indiv_id not in info['INDI']:
        return False

    # success case
    if 'FAMS' in info['INDI'][indiv_id]:
        return True

    return False


def s30_test(info, file):
    # This has been implemented for each individual
    file.write("\n\nList of living married individuals is: [ \n")
    for indiv in info['INDI']:
        if is_individual_living(info, indiv) and is_individual_married(info, indiv):
            file.write("{0} ({1}), \n".format(info['INDI'][indiv]['NAME'], indiv))

    file.write("]\n")
    return file


if __name__ == '__main__':
    unittest.main()
