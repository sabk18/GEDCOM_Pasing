"""
@author: Shivani Taneja
"""

import unittest
import datetime
from datetime import datetime


class RecentSurvivorsValidator(unittest.TestCase):

    def test_for_death_in_past_10_days(self):
        self.assertFalse(check_post_death_days('7 JAN 2020', 10))

    def test_for_death_in_past_20_days(self):
        self.assertFalse(check_post_death_days('9 FEB 2020', 20))

    def test_for_death_in_past_30_days(self):
        self.assertFalse(check_post_death_days('12 MAR 2020', 30))

    def test_for_not_recent_death(self):
        self.assertTrue(check_post_death_days('9 MAY 2018', 1000))

    def test_for_death_in_past_year(self):
        self.assertTrue(check_post_death_days('9 DEC 2019', 200))


def check_post_death_days(death_date, days):
    death_date = datetime.strptime(death_date, '%d %b %Y')
    current_date = datetime.now()
    number_of_days_post_death = (current_date - death_date).days

    if 0 <= number_of_days_post_death <= days:
        return True

    return False


def s36_test(info, file):
    # This has been implemented for each individual
    file.write("\n")
    for indiv in info['INDI']:
        if 'DEAT' in info['INDI'][indiv]:
            name = info['INDI'][indiv]['NAME']
            death_date = info['INDI'][indiv]['DEAT']
            if check_post_death_days(death_date, 30):
                file.write("\nInfo: INDI ID {0}, named {1}, died in the last 30 days".format(indiv, name))

    return file


if __name__ == '__main__':
    unittest.main()
