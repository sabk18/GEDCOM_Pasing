
"""
@author: Shivani Taneja
"""

import unittest
import datetime
from datetime import datetime, timedelta


class BirthBeforeParentDeathDateValidator(unittest.TestCase):

    def test_for_birth_after_mother_death(self):
        self.assertFalse(birth_before_parent_death('9 MAY 1990', '9 MAY 1989', 'mother'))

    def test_for_birth_before_mother_death(self):
        result = birth_before_parent_death('9 AUG 2018', '9 AUG 2019', 'mother')
        self.assertTrue(result)

    def test_for_birth_before_father_death(self):
        result = birth_before_parent_death('9 JAN 2002', '9 FEB 2009', 'father')
        self.assertTrue(result)

    def test_for_birth_before_9_months_father_death(self):
        result = birth_before_parent_death('9 AUG 2006', '9 FEB 2006', 'father')
        self.assertTrue(result)

    def test_for_birth_after_9_months_father_death(self):
        result = birth_before_parent_death('9 AUG 2010', '9 AUG 2009', 'father')
        self.assertFalse(result, datetime.now())


def birth_before_parent_death(child_birth_date, parent_death_date, relation):
    child_birth_date = datetime.strptime(child_birth_date, '%d %b %Y')
    parent_death_date = datetime.strptime(parent_death_date, '%d %b %Y')
    if relation == 'father' and child_birth_date >= (parent_death_date + timedelta(days=(9 * 365 / 12))):
        return False
    elif relation == 'mother' and child_birth_date >= parent_death_date:
        return False

    return True


def s09_test(info, file):
    # This has been implemented for each individual
    for indiv in info['INDI']:
        birth_date = info['INDI'][indiv]['BIRT']
        if 'FAMC' in info['INDI'][indiv]:
            family_id = info['INDI'][indiv]['FAMC']
            father_id = info['FAM'][family_id]['HUSB']
            mother_id = info['FAM'][family_id]['WIFE']

            if 'DEAT' in info['INDI'][father_id]:
                father_death_date = info['INDI'][father_id]['DEAT']
                if not birth_before_parent_death(birth_date, father_death_date, 'father'):
                    file.write("\nError: Birth Date of INDI ID {0}, After 9 months of Father's Death".format(indiv))
            if 'DEAT' in info['INDI'][mother_id]:
                mother_death_date = info['INDI'][mother_id]['DEAT']
                if not birth_before_parent_death(birth_date, mother_death_date, 'mother'):
                    file.write("\nError: Birth Date of INDI ID {0}, after Mother's Death".format(indiv))
    return file


if __name__ == '__main__':
    unittest.main()
