import unittest
import datetime
from datetime import datetime, timedelta


class MarriageBeforeDeath(unittest.TestCase):
    def test_checkifmarriageisless(self):
        result = testDates(datetime.now(), datetime.now() - timedelta(days=1))
        self.assertFalse(result)

def testDates(marriage, death):
    if not isinstance(death,datetime) or not isinstance(marriage, datetime):
        return False

    if death > marriage :
        return True
    else:
        return False

def s5test(info,file):
    for indiv in info['INDI']:
        if 'DEAT' in info['INDI']:
            death_date= info['INDI'][indiv]['DEAT']
            if not testDates(death_date,death_date):
                file.write("Error at DEAT Date at INDI ID {0} ".format(indiv))
    return file

if __name__ == '__main__':
    unittest.main()
