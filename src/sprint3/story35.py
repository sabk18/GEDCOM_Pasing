
"""
@author: Trevor Cardwell
"""
from tabulate import tabulate
import unittest
import datetime
from datetime import datetime
from datetime import date


class RecentBornValidator(unittest.TestCase):

    def testfullinput(self):
        self.assertTrue(
            s35_run({'INDI': {1: {'BIRT': '17 MAR 2020', 'FAMC': 2}}}, 1, True))

    def testdate(self):
        self.assertTrue(lessThanDays('17 MAR 2020', 30))

    def testlarge(self):
        self.assertFalse(lessThanDays('17 MAR 2010', 30))

    def testbad(self):
        self.assertFalse(lessThanDays('17 MAR 2010', 30))

    def testNull(self):
        self.assertFalse(lessThanDays(None, None))


def lessThanDays(date, num):
    try:
        return ((datetime.today()-datetime.strptime(date, '%d %b %Y')).days < num)
    except:
        return False


def s35_run(info, file, test=False):

    table = []
    for indiv in info['INDI']:
        if lessThanDays(info['INDI'][indiv]['BIRT'], 30):
            table.append([indiv, info['INDI'][indiv]['BIRT']])
    if test:
        return True
    file.write(tabulate(table, headers=['ID' 'Birthday', ], tablefmt="grid"))
    return file


if __name__ == '__main__':
    unittest.main()
