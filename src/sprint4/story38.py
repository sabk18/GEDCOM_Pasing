"""
@author: Shivani Taneja
"""

import unittest
import datetime
from datetime import datetime


class UpcomingBirthdayValidator(unittest.TestCase):
    def test_for_individual_living(self):
        self.assertTrue(is_individual_living({'INDI': {'@I6000123@': {'NAME': 'Dagar', 'SEX': 'M'}}},
                                             '@I6000123@'))

    def test_for_individual_living_another(self):
        self.assertFalse(is_individual_living({'INDI': {'@I8098234@': {'NAME': 'Taau Ji',
                                                                       'SEX' : 'M', 'DEAT': '9 FEB 1993'}}},
                                              '@I8098234@'))

    def test_for_birthday_in_next_10_days(self):
        self.assertFalse(check_upcoming_birthday('7 JAN 2021', 10))

    def test_for_birthday_in_next_20_days(self):
        self.assertFalse(check_upcoming_birthday('9 FEB 2021', 20))

    def test_for_birthday_in_next_30_days(self):
        self.assertFalse(check_upcoming_birthday('12 MAR 2021', 30))

    def test_for_not_recent_birthday(self):
        self.assertTrue(check_upcoming_birthday('9 FEB 2021', 300))


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


def calculate_dates(original_birth_date, now):
    delta1 = datetime(now.year, original_birth_date.month, original_birth_date.day)
    delta2 = datetime(now.year + 1, original_birth_date.month, original_birth_date.day)

    days = (delta1 - now).days if (delta1 - now).days > 0 else (delta2 - now).days
    # alternatively:
    # days = max(delta1, delta2).total_seconds() / 60 / 60 /24

    return days


def check_upcoming_birthday(birthday_date, days):
    birthday_date = datetime.strptime(birthday_date, '%d %b %Y')
    current_date = datetime.now()

    number_of_days_remaining_for_birthday = calculate_dates(birthday_date, current_date)

    if 0 <= number_of_days_remaining_for_birthday <= days:
        return True

    return False


def s38_test(info, file):
    # This has been implemented for each individual
    file.write("\n")
    for indiv in info['INDI']:
        if 'BIRT' in info['INDI'][indiv]:
            name = info['INDI'][indiv]['NAME']
            birthday_date = info['INDI'][indiv]['BIRT']
            if is_individual_living(info, indiv) and check_upcoming_birthday(birthday_date, 30):
                file.write("\nInfo: INDI ID {0}, named {1} and alive, has birthday in next 30 days".format(indiv, name))

    return file


if __name__ == '__main__':
    unittest.main()
