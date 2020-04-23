from tabulate import tabulate
import unittest
import datetime
from datetime import datetime, timedelta
from datetime import date


class upcommingAnValidator(unittest.TestCase):

    def testfullinput(self):
        self.assertTrue(
            s39_run({'FAM': {1: {'MAR': '17 OCT 2019', 'FAMC': 2}}}, 1, True))

    def testdate(self):
        self.assertFalse(lessThanDays('17 OCT 2019', 30))

    def testlarge(self):
        self.assertTrue(lessThanDays('17 MAY 2019', 30))

    def testbad(self):
        self.assertFalse(lessThanDays('17 MAR 2010', 30))

    def testNull(self):
        self.assertFalse(lessThanDays(None, None))


def lessThanDays(date, num):
    try:
        testdate = ((datetime.today()+timedelta(days=30))-(datetime.strptime(date, '%d %b %Y').replace(year=2020))).days
        return (testdate < 30 and testdate >= 0 )
    except:
        return False


def s39_run(info, file, test=False):



    for fam in info['FAM']:
        if lessThanDays(info['FAM'][fam]['MAR'], 30):
            if test:
                return True
            file.write('{} Has an upcomming Anniversary'.format(fam))
    if test:
        return True


    return file


if __name__ == '__main__':
    unittest.main()
